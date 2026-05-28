"""Google Sheets Integration via OAuth 2.0

Uses a Google Cloud OAuth 2.0 client for user-based authentication.
The user authorizes once, and the refresh token is stored for
subsequent automated weekly runs.

Setup Instructions:
1. Go to https://console.cloud.google.com/
2. Create a project → Enable Google Sheets API + Google Drive API
3. Create OAuth 2.0 Client ID (Desktop Application type)
4. Download the JSON and save as 'credentials.json' in the app directory
5. On first run, a browser will open for you to authorize
6. The token is saved as 'token.pickle' for subsequent runs
"""
import os
import pickle
import logging
from typing import Optional

import gspread
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

logger = logging.getLogger(__name__)

# Scopes needed for Google Sheets access
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
]


class GoogleSheetsManager:
    """Manages Google Sheets read/write operations with OAuth 2.0"""

    def __init__(self, credentials_file: str = 'credentials.json',
                 token_file: str = 'token.pickle'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self._client: Optional[gspread.Client] = None

    @property
    def client(self) -> gspread.Client:
        """Lazy-load and cache the authorized gspread client."""
        if self._client is None:
            self._client = self._authorize()
        return self._client

    @property
    def is_authorized(self) -> bool:
        """Check if we have valid credentials without triggering auth flow."""
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as f:
                creds = pickle.load(f)
            if creds and creds.valid:
                return True
            if creds and creds.expired and creds.refresh_token:
                return True  # Can refresh
        return False

    def _authorize(self) -> gspread.Client:
        """Authorize with Google OAuth 2.0.

        Uses a headless-friendly approach:
        - If token.pickle exists and is valid, use it.
        - If credentials.json exists but no token, use console-based flow
          (prints a URL the user visits to get an auth code).
        """
        creds = None

        # Load existing token
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as f:
                creds = pickle.load(f)
            logger.info("Loaded existing OAuth token")

        # Refresh or re-authorize
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logger.info("Refreshing expired OAuth token")
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    raise FileNotFoundError(
                        f"OAuth credentials file '{self.credentials_file}' not found. "
                        "Download it from Google Cloud Console (OAuth 2.0 Client ID → Desktop App)."
                    )

                # Use console-based flow (works on headless servers)
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES
                )
                # Use out-of-band (console) flow for headless servers
                # The redirect_uri is set to 'urn:ietf:wg:oauth:2.0:oob'
                flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

                auth_url, _ = flow.authorization_url(
                    access_type='offline',
                    prompt='consent',  # Always get refresh token
                    include_granted_scopes='true',
                )

                print("\n" + "=" * 60)
                print("GOOGLE SHEETS AUTHORIZATION REQUIRED")
                print("=" * 60)
                print(f"\nVisit this URL to authorize the app:\n\n{auth_url}\n")
                print("After authorizing, you'll receive an authorization code.")
                code = input("Enter the authorization code: ").strip()

                flow.fetch_token(code=code)
                creds = flow.credentials

            # Save the token for future runs
            with open(self.token_file, 'wb') as f:
                pickle.dump(creds, f)
            logger.info(f"OAuth token saved to {self.token_file}")

        return gspread.authorize(creds)

    # ── Spreadsheet Operations ──────────────────────────

    def get_or_create_sheet(self, spreadsheet_id: str, title: str = 'Price Data') -> gspread.Worksheet:
        """Get an existing sheet by title, or create it if it doesn't exist."""
        spreadsheet = self.client.open_by_key(spreadsheet_id)
        try:
            worksheet = spreadsheet.worksheet(title)
            logger.info(f"Using existing sheet: '{title}'")
        except gspread.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title, rows=1000, cols=30)
            logger.info(f"Created new sheet: '{title}'")
        return worksheet

    def append_weekly_data(self, spreadsheet_id: str, products: list[dict],
                           week_label: str) -> None:
        """Append a week's worth of product prices to the spreadsheet.

        Sheet structure (single sheet, week columns):
        Row 1 (header):  Product Name | Unit | 2026-W21 | 2026-W22 | ...
        Row 2+:          Apple        | 1kg  | Rs. 450  | Rs. 455  | ...

        Products are matched by name across weeks. New products get
        new rows. Existing products get their price in the newest column.
        """
        if not products:
            logger.warning("No products to write to sheet")
            return

        spreadsheet = self.client.open_by_key(spreadsheet_id)
        worksheet = self.get_or_create_sheet(spreadsheet_id)

        # Read existing data
        existing_data = worksheet.get_all_values()
        headers = existing_data[0] if existing_data else ['Product Name', 'Unit']
        data_rows = existing_data[1:] if len(existing_data) > 1 else []

        # Check if this week already exists (skip duplicate)
        if week_label in headers:
            logger.info(f"Week '{week_label}' already exists in sheet, skipping")
            return

        # Determine the new column index
        new_col_idx = len(headers) + 1  # 1-based for gspread
        headers.append(week_label)

        # Build lookup: product_name → row index
        product_row_map = {}
        for row_idx, row in enumerate(data_rows):
            if row and row[0].strip():
                product_row_map[row[0].strip().lower()] = row_idx + 2  # +2 for 1-based + header

        # Build updates as batch
        updates = []
        new_rows = []

        # Update header
        col_letter = self._col_letter(new_col_idx)
        updates.append({
            'range': f'{col_letter}1',
            'values': [[week_label]]
        })

        # Also update product count if this is first data column
        if len(headers) == 3:
            updates.append({
                'range': 'A1',
                'values': [['Product Name']]
            })
            updates.append({
                'range': 'B1',
                'values': [['Unit']]
            })

        # Process each product
        for product in products:
            name = product.get('name', '').strip()
            if not name:
                continue

            price_display = f"Rs. {product['current_price']:,.2f}" if product.get('current_price') else 'N/A'
            key = name.lower()

            if key in product_row_map:
                # Existing product: update just the new column
                row_num = product_row_map[key]
                updates.append({
                    'range': f'{col_letter}{row_num}',
                    'values': [[price_display]]
                })

                # Also update unit if we have it and current is empty
                unit = product.get('unit', '')
                if unit:
                    existing_unit = ''
                    if len(data_rows) > row_num - 2:
                        row_data = data_rows[row_num - 2]
                        existing_unit = row_data[1] if len(row_data) > 1 else ''
                    if not existing_unit:
                        updates.append({
                            'range': f'B{row_num}',
                            'values': [[unit]]
                        })
            else:
                # New product: add a row
                row_data = [name, product.get('unit', '')]
                # Pad with empty cells up to new column
                row_data.extend([''] * (new_col_idx - 3))
                row_data.append(price_display)
                new_rows.append(row_data)

        # Perform batch updates
        if updates:
            worksheet.batch_update(updates, value_input_option='USER_ENTERED')

        # Append new rows
        if new_rows:
            # Find next empty row
            next_row = len(data_rows) + 2  # 1-based, after header and existing
            # Extend sheet if needed
            current_rows = worksheet.row_count
            needed_rows = next_row + len(new_rows) - 1
            if needed_rows > current_rows:
                worksheet.add_rows(needed_rows - current_rows + 100)
            worksheet.update(
                f'A{next_row}',
                new_rows,
                value_input_option='USER_ENTERED'
            )

        # Update header row
        worksheet.update(
            'A1',
            [headers],
            value_input_option='USER_ENTERED'
        )

        logger.info(f"Sheet updated: {len(products)} products, "
                    f"{len(new_rows)} new, {len(updates) - 1} price updates")

    def create_new_sheet_with_headers(self, spreadsheet_id: str, title: str,
                                       products: list[dict], week_label: str) -> None:
        """Create a brand new sheet with proper headers and data (for initial setup)."""
        spreadsheet = self.client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.add_worksheet(title, rows=len(products) + 2, cols=20)

        headers = ['Product Name', 'Unit', 'Category', week_label, 'Image URL']
        worksheet.update('A1', [headers], value_input_option='USER_ENTERED')

        data = []
        for product in products:
            price_display = f"Rs. {product['current_price']:,.2f}" if product.get('current_price') else 'N/A'
            data.append([
                product.get('name', ''),
                product.get('unit', ''),
                product.get('category', ''),
                price_display,
                product.get('image_url', ''),
            ])

        if data:
            worksheet.update('A2', data, value_input_option='USER_ENTERED')

        logger.info(f"Created new sheet '{title}' with {len(data)} products")

    def test_connection(self, spreadsheet_id: str) -> dict:
        """Test the connection and return sheet info."""
        try:
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            worksheets = spreadsheet.worksheets()
            return {
                'success': True,
                'spreadsheet_title': spreadsheet.title,
                'worksheets': [ws.title for ws in worksheets],
                'row_count': worksheets[0].row_count if worksheets else 0,
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
            }

    @staticmethod
    def _col_letter(col_index: int) -> str:
        """Convert 1-based column index to letter(s). 1→A, 2→B, ..., 27→AA."""
        letters = ''
        while col_index > 0:
            col_index -= 1
            letters = chr(col_index % 26 + 65) + letters
            col_index //= 26
        return letters