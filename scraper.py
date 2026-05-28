<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-DHJF51F24N"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());

              gtag('config', 'G-DHJF51F24N');
            </script>
        

        <meta charset="utf-8">
        <title>scraper.py : /home/Dominicw/scraper.py : Editor : Dominicw : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="scraper.py : /home/Dominicw/scraper.py : Editor : Dominicw : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/output.c229730a84cf.css" type="text/css" media="screen">
        <link rel="stylesheet" href="/static/CACHE/css/output.b9a4961a16f7.css" type="text/css"><link rel="stylesheet" href="/static/CACHE/css/output.d4642a4a0e79.css" type="text/css" media="screen">

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "yEkNqHqIrMSE1jbbqq9StTiCvwCSF8cYqb5TO5HOQ9npYRnREz7a0fShe04V7BdY";
        </script>
        <script src="/static/CACHE/js/output.3a42bfc02f19.js"></script>
        

        <script src="/static/CACHE/js/output.d5f4ec83cdc0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Dominicw/files/home/Dominicw/scraper.py",
          check_hash: "/user/Dominicw/files/home/Dominicw/scraper.py",
          update_editor_mode_preference: "/user/Dominicw/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Dominicw/consoles/",
        });
        var filename = "/home/Dominicw/scraper.py";
        var hash = "5ba83a702ae9ac56fa2137c6a17fbe41";
        var interpreter = "python3.13";

        
            Anywhere.Editor.InitializeAce(ace, Anywhere.urls, filename, hash, interpreter, "pythonanywhere.com");
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/Dominicw/files/sharing/",
            csrfToken: "yEkNqHqIrMSE1jbbqq9StTiCvwCSF8cYqb5TO5HOQ9npYRnREz7a0fShe04V7BdY",
            path: "/home/Dominicw/scraper.py"
          }
        );

      });
    </script>

        

    </head>

    <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home/Dominicw" target="_parent">Dominicw</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">scraper.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
          
            <form class="reload_web_app" style="display: flex" method="POST" action="/user/Dominicw/webapps/Dominicw.pythonanywhere.com/reload">
              <button class="btn btn-default" type="submit" title="Reload Dominicw.pythonanywhere.com">
                <i class="glyphicon glyphicon-refresh"></i>
              </button>
              <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
              <div style="display: none; clear: both;" class="alert alert-danger error_message generic_error">
                There was a problem. If this keeps happening, please <a href="" class="feedback_link">send us feedback</a>.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message slow_startup_error">
                Your webapp took a long time to reload. It probably reloaded, but we were unable to check it.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message virtualenv_error">
                There is a problem with your virtualenv setup. Look at the <b>virtualenv</b> section on the web app tab for details.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message cname_error">
                There is a problem with your DNS configuration. Take a look at the <b>DNS setup</b> section on the web app tab for details.
              </div>
            </form>
          
        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  <li class=""><a id="id_dashboard_link" href="/user/Dominicw/">Dashboard</a></li>
  <li class=""><a id="id_consoles_link" href="/user/Dominicw/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/Dominicw/files/home/Dominicw">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/Dominicw/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/Dominicw/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/Dominicw/databases/">Databases</a></li>


        
<li class="">
        <a href="" data-testid="contact_support_link" target="_parent" class="feedback_link">
                
                Send Feedback
                
        </a>
</li>


<li class=""><a href="/forums/" target="_parent" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" target="_parent" class="help_link">Help</a>
</li>
<li class=""><a href="https://blog.pythonanywhere.com/" target="_parent" class="blog_link">Blog</a>
</li>


<li class=""><a href="/user/Dominicw/account/" target="_parent"
                class="account_link">Account</a></li>
<li class="">
        <form action="/logout/" method="POST" target="_parent">
                <input type="hidden" name="csrfmiddlewaretoken" value="yEkNqHqIrMSE1jbbqq9StTiCvwCSF8cYqb5TO5HOQ9npYRnREz7a0fShe04V7BdY">
                <button type="submit" class="btn-link logout_link">Log out</button>
        </form>
</li>

      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">&quot;&quot;&quot;Keells Super Website Scraper

Scrapes product listings from https://keellssuper.com
Uses multiple fallback strategies:
  1. API calls (preferred if GraphQL/REST endpoints available)
  2. HTML parsing of the rendered pages
  3. Sitemap exploration
&quot;&quot;&quot;
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
    &quot;&quot;&quot;Scrapes Keells Super website for product prices&quot;&quot;&quot;

    BASE_URL = &#39;https://keellssuper.com&#39;

    # ── Category Definitions ──────────────────────────
    # Maps category slugs to display names.
    # These are the URL path segments used on keellssuper.com.
    CATEGORIES = {
        # Fresh Produce
        &#39;fruits&#39;:            &#39;Fruits&#39;,
        &#39;vegetables&#39;:        &#39;Vegetables&#39;,
        # Meat &amp; Seafood
        &#39;meat-poultry&#39;:      &#39;Meat &amp; Poultry&#39;,
        &#39;seafood&#39;:           &#39;Seafood&#39;,
        # Dairy &amp; Bakery (keep to reasonable scope)
        # &#39;dairy&#39;:             &#39;Dairy&#39;,
        # &#39;bakery&#39;:            &#39;Bakery&#39;,
        # Staples &amp; Pantry
        &#39;rice-pulses&#39;:       &#39;Rice &amp; Pulses&#39;,
        &#39;oils-fats&#39;:         &#39;Oils &amp; Fats&#39;,
        &#39;spices-condiments&#39;: &#39;Spices &amp; Condiments&#39;,
        &#39;canned-food&#39;:       &#39;Canned &amp; Tinned&#39;,
        # Beverages
        &#39;beverages&#39;:         &#39;Beverages&#39;,
        # &#39;tea-coffee&#39;:        &#39;Tea &amp; Coffee&#39;,
        # &#39;juices&#39;:            &#39;Juices&#39;,
        # Snacks
        # &#39;snacks-confectionery&#39;: &#39;Snacks &amp; Confectionery&#39;,
        # &#39;biscuits-crackers&#39;:    &#39;Biscuits &amp; Crackers&#39;,
        # Household (for future expansion)
        # &#39;household-cleaning&#39;: &#39;Household &amp; Cleaning&#39;,
        # &#39;personal-care&#39;:      &#39;Personal Care&#39;,
    }

    # ── Category URL patterns ──────────────────────────
    # Keells Super uses multiple URL patterns. We&#39;ll try each.
    CATEGORY_URL_PATTERNS = [
        &#39;/product-category/{slug}/&#39;,
        &#39;/shop/{slug}/&#39;,
        &#39;/category/{slug}/&#39;,
        &#39;/collections/{slug}/&#39;,
        &#39;/{slug}/&#39;,
    ]

    # ── API Patterns ──────────────────────────────────
    # Many WooCommerce/Shopify/Next.js stores expose product APIs
    API_PATTERNS = [
        # WooCommerce REST API
        &#39;/wp-json/wc/v3/products?category={slug}&amp;per_page=100&amp;page={page}&#39;,
        # WooCommerce legacy
        &#39;/wp-json/wp/v2/product?product_cat={slug}&amp;per_page=100&amp;page={page}&#39;,
        # Shopify-style
        &#39;/collections/{slug}/products.json?page={page}&#39;,
        # Custom Next.js/Sanity
        &#39;/api/products?category={slug}&amp;page={page}&amp;limit=100&#39;,
        &#39;/api/catalog/products?category={slug}&amp;page={page}&amp;limit=100&#39;,
        # GraphQL-style (REST proxy)
        &#39;/api/graphql?query=products(category:&quot;{slug}&quot;)&#39;,
    ]

    def __init__(self, timeout: int = 30, delay: float = 0.5):
        self.timeout = timeout
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            &#39;User-Agent&#39;: &#39;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 &#39;
                          &#39;(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36&#39;,
            &#39;Accept&#39;: &#39;text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#39;,
            &#39;Accept-Language&#39;: &#39;en-US,en;q=0.5&#39;,
            &#39;Accept-Encoding&#39;: &#39;gzip, deflate, br&#39;,
            &#39;DNT&#39;: &#39;1&#39;,
            &#39;Connection&#39;: &#39;keep-alive&#39;,
            &#39;Upgrade-Insecure-Requests&#39;: &#39;1&#39;,
        })

    # ── Public API ──────────────────────────────────────
    def scrape_category(self, category_slug: str) -&gt; list[dict]:
        &quot;&quot;&quot;Scrape all products from a single category.

        Returns list of dicts with keys:
          name, current_price, original_price, unit, image_url, product_url
        &quot;&quot;&quot;
        products = []
        url = self._resolve_category_url(category_slug)

        if not url:
            logger.warning(f&quot;Could not resolve URL for category &#39;{category_slug}&#39;&quot;)
            return products

        logger.info(f&quot;Scraping category &#39;{category_slug}&#39; at {url}&quot;)

        # Strategy 1: Try direct API endpoints first (fast, structured)
        api_products = self._try_api_endpoints(category_slug)
        if api_products:
            logger.info(f&quot;  Got {len(api_products)} products via API for &#39;{category_slug}&#39;&quot;)
            return api_products

        # Strategy 2: Paginated HTML scraping
        page = 1
        while True:
            page_url = url if page == 1 else f&quot;{url}page/{page}/&quot;
            page_products, has_next = self._scrape_page(page_url, category_slug)
            products.extend(page_products)
            logger.info(f&quot;  Page {page}: {len(page_products)} products&quot;)
            if not has_next or not page_products:
                break
            page += 1
            time.sleep(self.delay)

        return products

    def scrape_all_categories(self) -&gt; dict[str, list[dict]]:
        &quot;&quot;&quot;Scrape all configured categories. Returns {category_name: [products]}.&quot;&quot;&quot;
        results = {}
        for slug, name in self.CATEGORIES.items():
            try:
                results[name] = self.scrape_category(slug)
                time.sleep(self.delay)
            except Exception as e:
                logger.error(f&quot;Failed to scrape &#39;{name}&#39;: {e}&quot;)
                results[name] = []
        return results

    # ── URL Resolution ─────────────────────────────────
    def _resolve_category_url(self, slug: str) -&gt; Optional[str]:
        &quot;&quot;&quot;Try different URL patterns to find the correct category URL.&quot;&quot;&quot;
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
            soup = BeautifulSoup(resp.text, &#39;lxml&#39;)
            for link in soup.find_all(&#39;a&#39;, href=True):
                href = link[&#39;href&#39;].lower()
                if slug.replace(&#39;-&#39;, &#39;&#39;) in href.replace(&#39;-&#39;, &#39;&#39;).replace(&#39;/&#39;, &#39;&#39;):
                    return urljoin(self.BASE_URL, link[&#39;href&#39;])
        except Exception:
            pass

        # Last resort: try the most common pattern
        return urljoin(self.BASE_URL, f&#39;/product-category/{slug}/&#39;)

    def _has_product_listings(self, html: str) -&gt; bool:
        &quot;&quot;&quot;Check if HTML contains product-like content.&quot;&quot;&quot;
        soup = BeautifulSoup(html, &#39;lxml&#39;)
        # Look for common product container classes
        product_selectors = [
            &#39;.product&#39;, &#39;.product-item&#39;, &#39;.product-card&#39;,
            &#39;[data-product-id]&#39;, &#39;.product-list-item&#39;,
            &#39;.goods-item&#39;, &#39;.item&#39;, &#39;article.product&#39;,
        ]
        for sel in product_selectors:
            if soup.select(sel):
                return True
        return False

    # ── API Strategy ───────────────────────────────────
    def _try_api_endpoints(self, slug: str) -&gt; Optional[list[dict]]:
        &quot;&quot;&quot;Try common REST/GraphQL API endpoints for product data.&quot;&quot;&quot;
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
                        if len(products) &lt; 100:  # Last page
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

    def _parse_api_response(self, data, slug: str) -&gt; list[dict]:
        &quot;&quot;&quot;Parse various API response formats into standardized product dicts.&quot;&quot;&quot;
        products = []

        # Handle different API response shapes
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            # Common wrapper keys
            items = (
                data.get(&#39;products&#39;) or
                data.get(&#39;data&#39;) or
                data.get(&#39;items&#39;) or
                data.get(&#39;results&#39;) or
                data.get(&#39;hits&#39;) or  # Algolia-style
                []
            )
            if isinstance(items, dict):
                items = items.get(&#39;edges&#39;, items.get(&#39;nodes&#39;, []))  # GraphQL relay
        else:
            return products

        for item in items:
            if isinstance(item, dict):
                # Try multiple key patterns for name
                name = (
                    item.get(&#39;name&#39;) or
                    item.get(&#39;title&#39;) or
                    item.get(&#39;product_name&#39;) or
                    item.get(&#39;productName&#39;) or
                    &#39;&#39;
                )

                # Price extraction
                price = self._extract_price(item.get(&#39;price&#39;))
                if price is None:
                    price = self._extract_price(item.get(&#39;regular_price&#39;))
                    if price is None:
                        price = self._extract_price(item.get(&#39;sale_price&#39;))

                original_price = self._extract_price(item.get(&#39;regular_price&#39;))
                if original_price is None:
                    original_price = self._extract_price(item.get(&#39;compare_at_price&#39;))

                # Unit / weight
                unit = (
                    item.get(&#39;unit&#39;) or
                    item.get(&#39;weight&#39;) or
                    item.get(&#39;size&#39;) or
                    item.get(&#39;variant&#39;) or
                    &#39;&#39;
                )

                # Image
                image_url = &#39;&#39;
                if item.get(&#39;images&#39;):
                    if isinstance(item[&#39;images&#39;], list) and len(item[&#39;images&#39;]) &gt; 0:
                        img = item[&#39;images&#39;][0]
                        image_url = img.get(&#39;src&#39;) or img.get(&#39;url&#39;) or &#39;&#39;
                    elif isinstance(item[&#39;images&#39;], str):
                        image_url = item[&#39;images&#39;]

                # Product URL
                product_url = (
                    item.get(&#39;permalink&#39;) or
                    item.get(&#39;url&#39;) or
                    item.get(&#39;link&#39;) or
                    &#39;&#39;
                )
                if product_url and not product_url.startswith(&#39;http&#39;):
                    product_url = urljoin(self.BASE_URL, product_url)

                if name and name.strip():
                    products.append({
                        &#39;name&#39;: name.strip(),
                        &#39;current_price&#39;: price or 0,
                        &#39;original_price&#39;: original_price or price or 0,
                        &#39;unit&#39;: str(unit).strip() if unit else &#39;&#39;,
                        &#39;image_url&#39;: str(image_url).strip() if image_url else &#39;&#39;,
                        &#39;product_url&#39;: str(product_url).strip() if product_url else &#39;&#39;,
                    })

        return products

    # ── HTML Scraping Strategy ─────────────────────────
    def _scrape_page(self, url: str, category_slug: str) -&gt; tuple[list[dict], bool]:
        &quot;&quot;&quot;Scrape a single category page. Returns (products, has_next_page).&quot;&quot;&quot;
        products = []
        try:
            resp = self.session.get(url, timeout=self.timeout)
            if resp.status_code != 200:
                return [], False
        except requests.RequestException as e:
            logger.warning(f&quot;  Request failed for {url}: {e}&quot;)
            return [], False

        soup = BeautifulSoup(resp.text, &#39;lxml&#39;)

        # Try multiple product card selectors (common e-commerce patterns)
        product_selectors = [
            &#39;.product&#39;, &#39;.product-item&#39;, &#39;.product-card&#39;, &#39;.product-list-item&#39;,
            &#39;article.product&#39;, &#39;.product-loop-item&#39;, &#39;.product-wrapper&#39;,
            &#39;[data-product-id]&#39;, &#39;.prd-item&#39;, &#39;.item-product&#39;,
            &#39;.goods-card&#39;, &#39;.goods-item&#39;, &#39;li.product&#39;, &#39;.product-grid-item&#39;,
            &#39;.product-container&#39;, &#39;.shop-item&#39;, &#39;figure.product&#39;,
            &#39;.col-product&#39;, &#39;.product-box&#39;, &#39;.product-tile&#39;,
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
            for img in soup.find_all(&#39;img&#39;):
                parent = img.find_parent([&#39;div&#39;, &#39;article&#39;, &#39;li&#39;, &#39;figure&#39;, &#39;a&#39;])
                if parent:
                    price_elem = parent.find(string=re.compile(r&#39;Rs\.?\s*[\d,]+\.?\d*|LKR\s*[\d,]+\.?\d*|[\d,]+\.[\d]{2}&#39;))
                    if price_elem:
                        product_cards.append(parent)

        for card in product_cards:
            try:
                product = self._parse_product_card(card)
                if product and product[&#39;name&#39;]:
                    products.append(product)
            except Exception as e:
                logger.debug(f&quot;  Failed to parse card: {e}&quot;)
                continue

        # Check for pagination (next page link)
        has_next = bool(
            soup.select(&#39;.next, .pagination .next, .page-numbers .next, [rel=&quot;next&quot;], .pagination__next&#39;) or
            soup.find(&#39;a&#39;, class_=re.compile(r&#39;next&#39;, re.I)) or
            soup.find(&#39;a&#39;, attrs={&#39;aria-label&#39;: re.compile(r&#39;next&#39;, re.I)})
        )

        # If no explicit pagination found but we got a full page, try page param
        if not has_next and len(products) &gt;= 20:
            has_next = True  # Assume there might be more

        return products, has_next

    def _parse_product_card(self, card) -&gt; Optional[dict]:
        &quot;&quot;&quot;Parse a single product card HTML element into a product dict.&quot;&quot;&quot;
        # Name extraction
        name = &#39;&#39;
        name_selectors = [
            &#39;.product-title&#39;, &#39;.product-name&#39;, &#39;.title&#39;, &#39;.name&#39;,
            &#39;h2&#39;, &#39;h3&#39;, &#39;h4&#39;, &#39;.product__title&#39;, &#39;.card-title&#39;,
            &#39;.product-card__title&#39;, &#39;[data-product-name]&#39;, &#39;.heading&#39;,
            &#39;.product-heading&#39;, &#39;.item-title&#39;, &#39;figcaption&#39;,
        ]
        for sel in name_selectors:
            elem = card.select_one(sel)
            if elem:
                name = elem.get_text(strip=True)
                if name:
                    break

        if not name:
            # Try alt text of image
            img = card.find(&#39;img&#39;)
            if img:
                name = img.get(&#39;alt&#39;, &#39;&#39;).strip()
                # Filter out non-product alt texts
                if name and len(name) &lt; 200:
                    pass
                else:
                    name = &#39;&#39;

        if not name or len(name) &lt; 2:
            return None

        # Price extraction - look for LKR/Rs patterns
        price = None
        original_price = None

        # Get all text from the card and find prices
        card_text = card.get_text(&#39; &#39;, strip=True)

        # Price patterns: Rs. 1,234.56 / LKR 1,234.56 / Rs.1234.56 / 1,234.56
        price_patterns = [
            r&#39;Rs\.?\s*([\d,]+\.?\d*)&#39;,
            r&#39;LKR\s*([\d,]+\.?\d*)&#39;,
            r&#39;රු\.?\s*([\d,]+\.?\d*)&#39;,  # Sinhala
            r&#39;₹\s*([\d,]+\.?\d*)&#39;,
            r&#39;([\d,]+\.\d{2})\s*(?:LKR|Rs|රු)?&#39;,
        ]

        all_prices = []
        for pat in price_patterns:
            matches = re.findall(pat, card_text, re.IGNORECASE)
            for m in matches:
                cleaned = m.replace(&#39;,&#39;, &#39;&#39;)
                try:
                    val = float(cleaned)
                    all_prices.append(val)
                except ValueError:
                    pass

        if all_prices:
            all_prices.sort()
            price = all_prices[0]  # Lowest = current/sale price
            if len(all_prices) &gt; 1:
                original_price = all_prices[-1]  # Highest = original price

        # Also check for strikethrough prices (original price)
        strike_elem = card.select_one(&#39;del, s, .old-price, .regular-price, .original-price, .was-price, .compare-price&#39;)
        if strike_elem:
            strike_text = strike_elem.get_text(strip=True)
            strike_match = re.search(r&#39;[\d,]+\.?\d*&#39;, strike_text)
            if strike_match:
                try:
                    strike_val = float(strike_match.group().replace(&#39;,&#39;, &#39;&#39;))
                    if original_price is None or strike_val &gt; original_price:
                        original_price = strike_val
                except ValueError:
                    pass

        # Unit/weight extraction
        unit = &#39;&#39;
        unit_selectors = [
            &#39;.product-weight&#39;, &#39;.product-size&#39;, &#39;.weight&#39;, &#39;.variant&#39;,
            &#39;.product-unit&#39;, &#39;.product-measure&#39;, &#39;.unit&#39;, &#39;.measure&#39;,
            &#39;.product-meta span&#39;, &#39;.variant-info&#39;,
        ]
        for sel in unit_selectors:
            elem = card.select_one(sel)
            if elem:
                unit = elem.get_text(strip=True)
                if unit:
                    break

        # If no explicit unit, try to find weight/volume in name or nearby text
        if not unit:
            unit_match = re.search(r&#39;(\d+\s*(?:g|kg|ml|l|L|pcs|pack|packet|tin|bottle|jar))&#39;, name, re.I)
            if unit_match:
                unit = unit_match.group(1)

        # Image URL
        image_url = &#39;&#39;
        img = card.find(&#39;img&#39;)
        if img:
            image_url = (img.get(&#39;data-src&#39;) or img.get(&#39;data-lazy-src&#39;) or
                        img.get(&#39;src&#39;) or img.get(&#39;data-original&#39;) or &#39;&#39;)

        # Product URL
        product_url = &#39;&#39;
        link = card.find(&#39;a&#39;, href=True)
        if link:
            href = link[&#39;href&#39;]
            if href and not href.startswith(&#39;#&#39;) and &#39;javascript:&#39; not in href:
                product_url = urljoin(self.BASE_URL, href)
        if not product_url and img:
            parent_a = img.find_parent(&#39;a&#39;)
            if parent_a and parent_a.get(&#39;href&#39;):
                product_url = urljoin(self.BASE_URL, parent_a[&#39;href&#39;])

        return {
            &#39;name&#39;: name.strip(),
            &#39;current_price&#39;: price or 0,
            &#39;original_price&#39;: original_price or price or 0,
            &#39;unit&#39;: unit.strip() if unit else &#39;&#39;,
            &#39;image_url&#39;: image_url.strip() if image_url else &#39;&#39;,
            &#39;product_url&#39;: product_url.strip() if product_url else &#39;&#39;,
        }

    # ── Helpers ────────────────────────────────────────
    @staticmethod
    def _extract_price(value) -&gt; Optional[float]:
        &quot;&quot;&quot;Extract a float from a price value (string, int, float).&quot;&quot;&quot;
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            match = re.search(r&#39;([\d,]+\.?\d*)&#39;, value.replace(&#39;,&#39;, &#39;&#39;))
            if match:
                return float(match.group(1))
        return None</div>
      

      <div id="id_ide_console">
        
          <div id="id_ide_console_pane_buttons">
            <center>
              
                <button class="btn btn-large btn-info run_button" title="Save &amp; Run (Ctrl + R)">&gt;&gt;&gt; Run this file</button>
                <button class="btn btn-large btn-info bash_console_here" title="Start a Bash console in this folder">$ Bash console here</button>
              
            </center>
          </div>
          <iframe style="display: none" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
          <div style="display: none;" class="console_limit_reached">
            <div class="container">
    <div class="row">
        <div class="col-md-5 col-md-offset-3 well">
            <h1>Console limit reached :-/</h1>

            <p>
            With your current PythonAnywhere account you can have up to
            2 consoles.  You can
            have more if you
            <a href="/user/Dominicw/account/">upgrade your account</a>!

            <p>
            Alternatively, if you don't feel like paying us more money, you
            can <a href="/user/Dominicw/consoles/">kill some consoles on your Consoles page</a>.
        </div>
    </div>
</div>


          </div>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        

<div id="id_feedback_dialog" title="Send Feedback"
    style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        
        Thank you for your feedback.
        
    </div>
    <div id="id_feedback_dialog_blurb_small">
        <!-- CTA disclaimer section -->
        
        <div id="id_cta_disclaimer" class="cta_disclaimer">
            <div id="id_disclaimer_text">
                We review all feedback, but we cannot promise a response.
                <br />
                <br />
                Did you know you can upgrade your plan to get access to Customer Support?
            </div>
            <div class="dialog_buttons center">
                <button class="btn btn-primary" id="id_feedback_dialog_upgrade_button"
                    onclick='window.top.location="/pricing/";'>
                    
                    Upgrade Now
                    
                </button>
            </div>
        </div>
        

        To help us assist you as efficiently as possible, please include:
        <ol>
            <li>What you were trying to do.</li>
            <li>What you expected to happen.</li>
            <li>What actually happened including any error messages or screenshots.</li>
            <li>Steps to reproduce the issue.</li>
        </ol>
    </div>

    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text"
        placeholder="Email address (optional - only necessary if you would like us to contact you)" />

    <div id="id_feedback_dialog_error" style="display: none">
        Sorry, there was a problem connecting to the server. Please try again in a few moments.
    </div>
    <div id="id_feedback_dialog_rate_limit_error" style="display: none">
        
        Sorry, you have reached the sending limit for feedback. Please try again in a few moments.
        
    </div>
    <div id="id_feedback_dialog_success" style="display: none">
        
        Thank you for your feedback. We review all feedback, but we cannot promise a response.
        
    </div>

    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>

    <div id="id_feedback_dialog_only_close_button" style="display: none">
        <button class="btn btn-primary" id="id_feedback_dialog_close_button">Close</button>
    </div>
</div>

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
