"""Keells Super Website Scraper

Scrapes product listings from https://keellssuper.com
Uses multiple fallback strategies:
  1. API calls (preferred if GraphQL/REST endpoints available)
  2. HTML parsing of the rendered pages
  3. Sitemap exploration
"""
import re
import time
import json
import logging
from urllib.parse import urljoin, urlparse
from typing import Optional

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class KeellsScraper:
    """Scrapes Keells Super website for product prices"""

    BASE_URL = 'https://keellssuper.com'

    # ── Category Definitions ──────────────────────────
    # Maps category slugs to display names.
    # These are the URL path segments used on keellssuper.com.
    CATEGORIES = {
        # Fresh Produce
        'fruits':            'Fruits',
        'vegetables':        'Vegetables',
        # Meat & Seafood
        'meat-poultry':      'Meat & Poultry',
        'seafood':           'Seafood',
        # Dairy & Bakery (keep to reasonable scope)
        # 'dairy':             'Dairy',
        # 'bakery':            'Bakery',
        # Staples & Pantry
        'rice-pulses':       'Rice & Pulses',
        'oils-fats':         'Oils & Fats',
        'spices-condiments': 'Spices & Condiments',
        'canned-food':       'Canned & Tinned',
        # Beverages
        'beverages':         'Beverages',
        # 'tea-coffee':        'Tea & Coffee',
        # 'juices':            'Juices',
        # Snacks
        # 'snacks-confectionery': 'Snacks & Confectionery',
        # 'biscuits-crackers':    'Biscuits & Crackers',
        # Household (for future expansion)
        # 'household-cleaning': 'Household & Cleaning',
        # 'personal-care':      'Personal Care',
    }

    # ── Category URL patterns ──────────────────────────
    # Keells Super uses multiple URL patterns. We'll try each.
    CATEGORY_URL_PATTERNS = [
        '/product-category/{slug}/',
        '/shop/{slug}/',
        '/category/{slug}/',
        '/collections/{slug}/',
        '/{slug}/',
    ]

    # ── API Patterns ──────────────────────────────────
    # Many WooCommerce/Shopify/Next.js stores expose product APIs
    API_PATTERNS = [
        # WooCommerce REST API
        '/wp-json/wc/v3/products?category={slug}&per_page=100&page={page}',
        # WooCommerce legacy
        '/wp-json/wp/v2/product?product_cat={slug}&per_page=100&page={page}',
        # Shopify-style
        '/collections/{slug}/products.json?page={page}',
        # Custom Next.js/Sanity
        '/api/products?category={slug}&page={page}&limit=100',
        '/api/catalog/products?category={slug}&page={page}&limit=100',
        # GraphQL-style (REST proxy)
        '/api/graphql?query=products(category:"{slug}")',
    ]

    def __init__(self, timeout: int = 30, delay: float = 0.5):
        self.timeout = timeout
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })

    # ── Public API ──────────────────────────────────────
    def scrape_category(self, category_slug: str) -> list[dict]:
        """Scrape all products from a single category.

        Returns list of dicts with keys:
          name, current_price, original_price, unit, image_url, product_url
        """
        products = []
        url = self._resolve_category_url(category_slug)

        if not url:
            logger.warning(f"Could not resolve URL for category '{category_slug}'")
            return products

        logger.info(f"Scraping category '{category_slug}' at {url}")

        # Strategy 1: Try direct API endpoints first (fast, structured)
        api_products = self._try_api_endpoints(category_slug)
        if api_products:
            logger.info(f"  Got {len(api_products)} products via API for '{category_slug}'")
            return api_products

        # Strategy 2: Paginated HTML scraping
        page = 1
        while True:
            page_url = url if page == 1 else f"{url}page/{page}/"
            page_products, has_next = self._scrape_page(page_url, category_slug)
            products.extend(page_products)
            logger.info(f"  Page {page}: {len(page_products)} products")
            if not has_next or not page_products:
                break
            page += 1
            time.sleep(self.delay)

        return products

    def scrape_all_categories(self) -> dict[str, list[dict]]:
        """Scrape all configured categories. Returns {category_name: [products]}."""
        results = {}
        for slug, name in self.CATEGORIES.items():
            try:
                results[name] = self.scrape_category(slug)
                time.sleep(self.delay)
            except Exception as e:
                logger.error(f"Failed to scrape '{name}': {e}")
                results[name] = []
        return results

    # ── URL Resolution ─────────────────────────────────
    def _resolve_category_url(self, slug: str) -> Optional[str]:
        """Try different URL patterns to find the correct category URL."""
        for pattern in self.CATEGORY_URL_PATTERNS:
            url = urljoin(self.BASE_URL, pattern.format(slug=slug))
            try:
                resp = self.session.get(url, timeout=self.timeout, allow_redirects=True)
                if resp.status_code == 200 and self._has_product_listings(resp.text):
                    return resp.url  # Use final URL after redirects
            except requests.RequestException:
                continue

        # Fallback: try fetching the homepage and finding category links
        try:
            resp = self.session.get(self.BASE_URL, timeout=self.timeout)
            soup = BeautifulSoup(resp.text, 'lxml')
            for link in soup.find_all('a', href=True):
                href = link['href'].lower()
                if slug.replace('-', '') in href.replace('-', '').replace('/', ''):
                    return urljoin(self.BASE_URL, link['href'])
        except Exception:
            pass

        # Last resort: try the most common pattern
        return urljoin(self.BASE_URL, f'/product-category/{slug}/')

    def _has_product_listings(self, html: str) -> bool:
        """Check if HTML contains product-like content."""
        soup = BeautifulSoup(html, 'lxml')
        # Look for common product container classes
        product_selectors = [
            '.product', '.product-item', '.product-card',
            '[data-product-id]', '.product-list-item',
            '.goods-item', '.item', 'article.product',
        ]
        for sel in product_selectors:
            if soup.select(sel):
                return True
        return False

    # ── API Strategy ───────────────────────────────────
    def _try_api_endpoints(self, slug: str) -> Optional[list[dict]]:
        """Try common REST/GraphQL API endpoints for product data."""
        for pattern in self.API_PATTERNS:
            page = 1
            all_products = []
            while True:
                url = urljoin(self.BASE_URL, pattern.format(slug=slug, page=page))
                try:
                    resp = self.session.get(url, timeout=self.timeout)
                    if resp.status_code == 200:
                        products = self._parse_api_response(resp.json(), slug)
                        if not products:
                            break
                        all_products.extend(products)
                        if len(products) < 100:  # Last page
                            break
                        page += 1
                        time.sleep(0.3)
                    else:
                        break
                except (requests.RequestException, json.JSONDecodeError, ValueError):
                    break

            if all_products:
                return all_products
        return None

    def _parse_api_response(self, data, slug: str) -> list[dict]:
        """Parse various API response formats into standardized product dicts."""
        products = []

        # Handle different API response shapes
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            # Common wrapper keys
            items = (
                data.get('products') or
                data.get('data') or
                data.get('items') or
                data.get('results') or
                data.get('hits') or  # Algolia-style
                []
            )
            if isinstance(items, dict):
                items = items.get('edges', items.get('nodes', []))  # GraphQL relay
        else:
            return products

        for item in items:
            if isinstance(item, dict):
                # Try multiple key patterns for name
                name = (
                    item.get('name') or
                    item.get('title') or
                    item.get('product_name') or
                    item.get('productName') or
                    ''
                )

                # Price extraction
                price = self._extract_price(item.get('price'))
                if price is None:
                    price = self._extract_price(item.get('regular_price'))
                    if price is None:
                        price = self._extract_price(item.get('sale_price'))

                original_price = self._extract_price(item.get('regular_price'))
                if original_price is None:
                    original_price = self._extract_price(item.get('compare_at_price'))

                # Unit / weight
                unit = (
                    item.get('unit') or
                    item.get('weight') or
                    item.get('size') or
                    item.get('variant') or
                    ''
                )

                # Image
                image_url = ''
                if item.get('images'):
                    if isinstance(item['images'], list) and len(item['images']) > 0:
                        img = item['images'][0]
                        image_url = img.get('src') or img.get('url') or ''
                    elif isinstance(item['images'], str):
                        image_url = item['images']

                # Product URL
                product_url = (
                    item.get('permalink') or
                    item.get('url') or
                    item.get('link') or
                    ''
                )
                if product_url and not product_url.startswith('http'):
                    product_url = urljoin(self.BASE_URL, product_url)

                if name and name.strip():
                    products.append({
                        'name': name.strip(),
                        'current_price': price or 0,
                        'original_price': original_price or price or 0,
                        'unit': str(unit).strip() if unit else '',
                        'image_url': str(image_url).strip() if image_url else '',
                        'product_url': str(product_url).strip() if product_url else '',
                    })

        return products

    # ── HTML Scraping Strategy ─────────────────────────
    def _scrape_page(self, url: str, category_slug: str) -> tuple[list[dict], bool]:
        """Scrape a single category page. Returns (products, has_next_page)."""
        products = []
        try:
            resp = self.session.get(url, timeout=self.timeout)
            if resp.status_code != 200:
                return [], False
        except requests.RequestException as e:
            logger.warning(f"  Request failed for {url}: {e}")
            return [], False

        soup = BeautifulSoup(resp.text, 'lxml')

        # Try multiple product card selectors (common e-commerce patterns)
        product_selectors = [
            '.product', '.product-item', '.product-card', '.product-list-item',
            'article.product', '.product-loop-item', '.product-wrapper',
            '[data-product-id]', '.prd-item', '.item-product',
            '.goods-card', '.goods-item', 'li.product', '.product-grid-item',
            '.product-container', '.shop-item', 'figure.product',
            '.col-product', '.product-box', '.product-tile',
        ]

        product_cards = []
        for sel in product_selectors:
            cards = soup.select(sel)
            if cards:
                product_cards = cards
                break

        # If no product cards found with known selectors, try generic grid
        if not product_cards:
            # Look for repeated patterns: images with nearby prices
            for img in soup.find_all('img'):
                parent = img.find_parent(['div', 'article', 'li', 'figure', 'a'])
                if parent:
                    price_elem = parent.find(string=re.compile(r'Rs\.?\s*[\d,]+\.?\d*|LKR\s*[\d,]+\.?\d*|[\d,]+\.[\d]{2}'))
                    if price_elem:
                        product_cards.append(parent)

        for card in product_cards:
            try:
                product = self._parse_product_card(card)
                if product and product['name']:
                    products.append(product)
            except Exception as e:
                logger.debug(f"  Failed to parse card: {e}")
                continue

        # Check for pagination (next page link)
        has_next = bool(
            soup.select('.next, .pagination .next, .page-numbers .next, [rel="next"], .pagination__next') or
            soup.find('a', class_=re.compile(r'next', re.I)) or
            soup.find('a', attrs={'aria-label': re.compile(r'next', re.I)})
        )

        # If no explicit pagination found but we got a full page, try page param
        if not has_next and len(products) >= 20:
            has_next = True  # Assume there might be more

        return products, has_next

    def _parse_product_card(self, card) -> Optional[dict]:
        """Parse a single product card HTML element into a product dict."""
        # Name extraction
        name = ''
        name_selectors = [
            '.product-title', '.product-name', '.title', '.name',
            'h2', 'h3', 'h4', '.product__title', '.card-title',
            '.product-card__title', '[data-product-name]', '.heading',
            '.product-heading', '.item-title', 'figcaption',
        ]
        for sel in name_selectors:
            elem = card.select_one(sel)
            if elem:
                name = elem.get_text(strip=True)
                if name:
                    break

        if not name:
            # Try alt text of image
            img = card.find('img')
            if img:
                name = img.get('alt', '').strip()
                # Filter out non-product alt texts
                if name and len(name) < 200:
                    pass
                else:
                    name = ''

        if not name or len(name) < 2:
            return None

        # Price extraction - look for LKR/Rs patterns
        price = None
        original_price = None

        # Get all text from the card and find prices
        card_text = card.get_text(' ', strip=True)

        # Price patterns: Rs. 1,234.56 / LKR 1,234.56 / Rs.1234.56 / 1,234.56
        price_patterns = [
            r'Rs\.?\s*([\d,]+\.?\d*)',
            r'LKR\s*([\d,]+\.?\d*)',
            r'රු\.?\s*([\d,]+\.?\d*)',  # Sinhala
            r'₹\s*([\d,]+\.?\d*)',
            r'([\d,]+\.\d{2})\s*(?:LKR|Rs|රු)?',
        ]

        all_prices = []
        for pat in price_patterns:
            matches = re.findall(pat, card_text, re.IGNORECASE)
            for m in matches:
                cleaned = m.replace(',', '')
                try:
                    val = float(cleaned)
                    all_prices.append(val)
                except ValueError:
                    pass

        if all_prices:
            all_prices.sort()
            price = all_prices[0]  # Lowest = current/sale price
            if len(all_prices) > 1:
                original_price = all_prices[-1]  # Highest = original price

        # Also check for strikethrough prices (original price)
        strike_elem = card.select_one('del, s, .old-price, .regular-price, .original-price, .was-price, .compare-price')
        if strike_elem:
            strike_text = strike_elem.get_text(strip=True)
            strike_match = re.search(r'[\d,]+\.?\d*', strike_text)
            if strike_match:
                try:
                    strike_val = float(strike_match.group().replace(',', ''))
                    if original_price is None or strike_val > original_price:
                        original_price = strike_val
                except ValueError:
                    pass

        # Unit/weight extraction
        unit = ''
        unit_selectors = [
            '.product-weight', '.product-size', '.weight', '.variant',
            '.product-unit', '.product-measure', '.unit', '.measure',
            '.product-meta span', '.variant-info',
        ]
        for sel in unit_selectors:
            elem = card.select_one(sel)
            if elem:
                unit = elem.get_text(strip=True)
                if unit:
                    break

        # If no explicit unit, try to find weight/volume in name or nearby text
        if not unit:
            unit_match = re.search(r'(\d+\s*(?:g|kg|ml|l|L|pcs|pack|packet|tin|bottle|jar))', name, re.I)
            if unit_match:
                unit = unit_match.group(1)

        # Image URL
        image_url = ''
        img = card.find('img')
        if img:
            image_url = (img.get('data-src') or img.get('data-lazy-src') or
                        img.get('src') or img.get('data-original') or '')

        # Product URL
        product_url = ''
        link = card.find('a', href=True)
        if link:
            href = link['href']
            if href and not href.startswith('#') and 'javascript:' not in href:
                product_url = urljoin(self.BASE_URL, href)
        if not product_url and img:
            parent_a = img.find_parent('a')
            if parent_a and parent_a.get('href'):
                product_url = urljoin(self.BASE_URL, parent_a['href'])

        return {
            'name': name.strip(),
            'current_price': price or 0,
            'original_price': original_price or price or 0,
            'unit': unit.strip() if unit else '',
            'image_url': image_url.strip() if image_url else '',
            'product_url': product_url.strip() if product_url else '',
        }

    # ── Helpers ────────────────────────────────────────
    @staticmethod
    def _extract_price(value) -> Optional[float]:
        """Extract a float from a price value (string, int, float)."""
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            match = re.search(r'([\d,]+\.?\d*)', value.replace(',', ''))
            if match:
                return float(match.group(1))
        return None