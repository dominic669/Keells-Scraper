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
        <title>sheets.py : /home/Dominicw/sheets.py : Editor : Dominicw : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="sheets.py : /home/Dominicw/sheets.py : Editor : Dominicw : PythonAnywhere">
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
            Anywhere.csrfToken = "aAFw4Wkd1MjRloZwcuLK9MIJOs1HTMjq27qCskBjq9OCiWbcqDJ2G8ioxWtKlfkq";
        </script>
        <script src="/static/CACHE/js/output.3a42bfc02f19.js"></script>
        

        <script src="/static/CACHE/js/output.d5f4ec83cdc0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Dominicw/files/home/Dominicw/sheets.py",
          check_hash: "/user/Dominicw/files/home/Dominicw/sheets.py",
          update_editor_mode_preference: "/user/Dominicw/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Dominicw/consoles/",
        });
        var filename = "/home/Dominicw/sheets.py";
        var hash = "42ff28d60af88bd387a6b8effc5d891c";
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
            csrfToken: "aAFw4Wkd1MjRloZwcuLK9MIJOs1HTMjq27qCskBjq9OCiWbcqDJ2G8ioxWtKlfkq",
            path: "/home/Dominicw/sheets.py"
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
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home/Dominicw" target="_parent">Dominicw</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">sheets.py</span></span>

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
                <input type="hidden" name="csrfmiddlewaretoken" value="aAFw4Wkd1MjRloZwcuLK9MIJOs1HTMjq27qCskBjq9OCiWbcqDJ2G8ioxWtKlfkq">
                <button type="submit" class="btn-link logout_link">Log out</button>
        </form>
</li>

      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">&quot;&quot;&quot;Google Sheets Integration via OAuth 2.0

Uses a Google Cloud OAuth 2.0 client for user-based authentication.
The user authorizes once, and the refresh token is stored for
subsequent automated weekly runs.

Setup Instructions:
1. Go to https://console.cloud.google.com/
2. Create a project → Enable Google Sheets API + Google Drive API
3. Create OAuth 2.0 Client ID (Desktop Application type)
4. Download the JSON and save as &#39;credentials.json&#39; in the app directory
5. On first run, a browser will open for you to authorize
6. The token is saved as &#39;token.pickle&#39; for subsequent runs
&quot;&quot;&quot;
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
    &#39;https://www.googleapis.com/auth/spreadsheets&#39;,
    &#39;https://www.googleapis.com/auth/drive.file&#39;,
]


class GoogleSheetsManager:
    &quot;&quot;&quot;Manages Google Sheets read/write operations with OAuth 2.0&quot;&quot;&quot;

    def __init__(self, credentials_file: str = &#39;credentials.json&#39;,
                 token_file: str = &#39;token.pickle&#39;):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self._client: Optional[gspread.Client] = None

    @property
    def client(self) -&gt; gspread.Client:
        &quot;&quot;&quot;Lazy-load and cache the authorized gspread client.&quot;&quot;&quot;
        if self._client is None:
            self._client = self._authorize()
        return self._client

    @property
    def is_authorized(self) -&gt; bool:
        &quot;&quot;&quot;Check if we have valid credentials without triggering auth flow.&quot;&quot;&quot;
        if os.path.exists(self.token_file):
            with open(self.token_file, &#39;rb&#39;) as f:
                creds = pickle.load(f)
            if creds and creds.valid:
                return True
            if creds and creds.expired and creds.refresh_token:
                return True  # Can refresh
        return False

    def _authorize(self) -&gt; gspread.Client:
        &quot;&quot;&quot;Authorize with Google OAuth 2.0.

        Uses a headless-friendly approach:
        - If token.pickle exists and is valid, use it.
        - If credentials.json exists but no token, use console-based flow
          (prints a URL the user visits to get an auth code).
        &quot;&quot;&quot;
        creds = None

        # Load existing token
        if os.path.exists(self.token_file):
            with open(self.token_file, &#39;rb&#39;) as f:
                creds = pickle.load(f)
            logger.info(&quot;Loaded existing OAuth token&quot;)

        # Refresh or re-authorize
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logger.info(&quot;Refreshing expired OAuth token&quot;)
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    raise FileNotFoundError(
                        f&quot;OAuth credentials file &#39;{self.credentials_file}&#39; not found. &quot;
                        &quot;Download it from Google Cloud Console (OAuth 2.0 Client ID → Desktop App).&quot;
                    )

                # Use console-based flow (works on headless servers)
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES
                )
                # Use out-of-band (console) flow for headless servers
                # The redirect_uri is set to &#39;urn:ietf:wg:oauth:2.0:oob&#39;
                flow.redirect_uri = &#39;urn:ietf:wg:oauth:2.0:oob&#39;

                auth_url, _ = flow.authorization_url(
                    access_type=&#39;offline&#39;,
                    prompt=&#39;consent&#39;,  # Always get refresh token
                    include_granted_scopes=&#39;true&#39;,
                )

                print(&quot;\n&quot; + &quot;=&quot; * 60)
                print(&quot;GOOGLE SHEETS AUTHORIZATION REQUIRED&quot;)
                print(&quot;=&quot; * 60)
                print(f&quot;\nVisit this URL to authorize the app:\n\n{auth_url}\n&quot;)
                print(&quot;After authorizing, you&#39;ll receive an authorization code.&quot;)
                code = input(&quot;Enter the authorization code: &quot;).strip()

                flow.fetch_token(code=code)
                creds = flow.credentials

            # Save the token for future runs
            with open(self.token_file, &#39;wb&#39;) as f:
                pickle.dump(creds, f)
            logger.info(f&quot;OAuth token saved to {self.token_file}&quot;)

        return gspread.authorize(creds)

    # ── Spreadsheet Operations ──────────────────────────

    def get_or_create_sheet(self, spreadsheet_id: str, title: str = &#39;Price Data&#39;) -&gt; gspread.Worksheet:
        &quot;&quot;&quot;Get an existing sheet by title, or create it if it doesn&#39;t exist.&quot;&quot;&quot;
        spreadsheet = self.client.open_by_key(spreadsheet_id)
        try:
            worksheet = spreadsheet.worksheet(title)
            logger.info(f&quot;Using existing sheet: &#39;{title}&#39;&quot;)
        except gspread.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title, rows=1000, cols=30)
            logger.info(f&quot;Created new sheet: &#39;{title}&#39;&quot;)
        return worksheet

    def append_weekly_data(self, spreadsheet_id: str, products: list[dict],
                           week_label: str) -&gt; None:
        &quot;&quot;&quot;Append a week&#39;s worth of product prices to the spreadsheet.

        Sheet structure (single sheet, week columns):
        Row 1 (header):  Product Name | Unit | 2026-W21 | 2026-W22 | ...
        Row 2+:          Apple        | 1kg  | Rs. 450  | Rs. 455  | ...

        Products are matched by name across weeks. New products get
        new rows. Existing products get their price in the newest column.
        &quot;&quot;&quot;
        if not products:
            logger.warning(&quot;No products to write to sheet&quot;)
            return

        spreadsheet = self.client.open_by_key(spreadsheet_id)
        worksheet = self.get_or_create_sheet(spreadsheet_id)

        # Read existing data
        existing_data = worksheet.get_all_values()
        headers = existing_data[0] if existing_data else [&#39;Product Name&#39;, &#39;Unit&#39;]
        data_rows = existing_data[1:] if len(existing_data) &gt; 1 else []

        # Check if this week already exists (skip duplicate)
        if week_label in headers:
            logger.info(f&quot;Week &#39;{week_label}&#39; already exists in sheet, skipping&quot;)
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
            &#39;range&#39;: f&#39;{col_letter}1&#39;,
            &#39;values&#39;: [[week_label]]
        })

        # Also update product count if this is first data column
        if len(headers) == 3:
            updates.append({
                &#39;range&#39;: &#39;A1&#39;,
                &#39;values&#39;: [[&#39;Product Name&#39;]]
            })
            updates.append({
                &#39;range&#39;: &#39;B1&#39;,
                &#39;values&#39;: [[&#39;Unit&#39;]]
            })

        # Process each product
        for product in products:
            name = product.get(&#39;name&#39;, &#39;&#39;).strip()
            if not name:
                continue

            price_display = f&quot;Rs. {product[&#39;current_price&#39;]:,.2f}&quot; if product.get(&#39;current_price&#39;) else &#39;N/A&#39;
            key = name.lower()

            if key in product_row_map:
                # Existing product: update just the new column
                row_num = product_row_map[key]
                updates.append({
                    &#39;range&#39;: f&#39;{col_letter}{row_num}&#39;,
                    &#39;values&#39;: [[price_display]]
                })

                # Also update unit if we have it and current is empty
                unit = product.get(&#39;unit&#39;, &#39;&#39;)
                if unit:
                    existing_unit = &#39;&#39;
                    if len(data_rows) &gt; row_num - 2:
                        row_data = data_rows[row_num - 2]
                        existing_unit = row_data[1] if len(row_data) &gt; 1 else &#39;&#39;
                    if not existing_unit:
                        updates.append({
                            &#39;range&#39;: f&#39;B{row_num}&#39;,
                            &#39;values&#39;: [[unit]]
                        })
            else:
                # New product: add a row
                row_data = [name, product.get(&#39;unit&#39;, &#39;&#39;)]
                # Pad with empty cells up to new column
                row_data.extend([&#39;&#39;] * (new_col_idx - 3))
                row_data.append(price_display)
                new_rows.append(row_data)

        # Perform batch updates
        if updates:
            worksheet.batch_update(updates, value_input_option=&#39;USER_ENTERED&#39;)

        # Append new rows
        if new_rows:
            # Find next empty row
            next_row = len(data_rows) + 2  # 1-based, after header and existing
            # Extend sheet if needed
            current_rows = worksheet.row_count
            needed_rows = next_row + len(new_rows) - 1
            if needed_rows &gt; current_rows:
                worksheet.add_rows(needed_rows - current_rows + 100)
            worksheet.update(
                f&#39;A{next_row}&#39;,
                new_rows,
                value_input_option=&#39;USER_ENTERED&#39;
            )

        # Update header row
        worksheet.update(
            &#39;A1&#39;,
            [headers],
            value_input_option=&#39;USER_ENTERED&#39;
        )

        logger.info(f&quot;Sheet updated: {len(products)} products, &quot;
                    f&quot;{len(new_rows)} new, {len(updates) - 1} price updates&quot;)

    def create_new_sheet_with_headers(self, spreadsheet_id: str, title: str,
                                       products: list[dict], week_label: str) -&gt; None:
        &quot;&quot;&quot;Create a brand new sheet with proper headers and data (for initial setup).&quot;&quot;&quot;
        spreadsheet = self.client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.add_worksheet(title, rows=len(products) + 2, cols=20)

        headers = [&#39;Product Name&#39;, &#39;Unit&#39;, &#39;Category&#39;, week_label, &#39;Image URL&#39;]
        worksheet.update(&#39;A1&#39;, [headers], value_input_option=&#39;USER_ENTERED&#39;)

        data = []
        for product in products:
            price_display = f&quot;Rs. {product[&#39;current_price&#39;]:,.2f}&quot; if product.get(&#39;current_price&#39;) else &#39;N/A&#39;
            data.append([
                product.get(&#39;name&#39;, &#39;&#39;),
                product.get(&#39;unit&#39;, &#39;&#39;),
                product.get(&#39;category&#39;, &#39;&#39;),
                price_display,
                product.get(&#39;image_url&#39;, &#39;&#39;),
            ])

        if data:
            worksheet.update(&#39;A2&#39;, data, value_input_option=&#39;USER_ENTERED&#39;)

        logger.info(f&quot;Created new sheet &#39;{title}&#39; with {len(data)} products&quot;)

    def test_connection(self, spreadsheet_id: str) -&gt; dict:
        &quot;&quot;&quot;Test the connection and return sheet info.&quot;&quot;&quot;
        try:
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            worksheets = spreadsheet.worksheets()
            return {
                &#39;success&#39;: True,
                &#39;spreadsheet_title&#39;: spreadsheet.title,
                &#39;worksheets&#39;: [ws.title for ws in worksheets],
                &#39;row_count&#39;: worksheets[0].row_count if worksheets else 0,
            }
        except Exception as e:
            return {
                &#39;success&#39;: False,
                &#39;error&#39;: str(e),
            }

    @staticmethod
    def _col_letter(col_index: int) -&gt; str:
        &quot;&quot;&quot;Convert 1-based column index to letter(s). 1→A, 2→B, ..., 27→AA.&quot;&quot;&quot;
        letters = &#39;&#39;
        while col_index &gt; 0:
            col_index -= 1
            letters = chr(col_index % 26 + 65) + letters
            col_index //= 26
        return letters</div>
      

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
