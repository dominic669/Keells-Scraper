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
        <title>app.py : /home/Dominicw/app.py : Editor : Dominicw : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="app.py : /home/Dominicw/app.py : Editor : Dominicw : PythonAnywhere">
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
            Anywhere.csrfToken = "QlDOk6xM0Q7KTWhlZ6r5YKcdnlQ3X6l5ISoUIuOSpdCvQut1dfpnv6MS6Pi6pzm5";
        </script>
        <script src="/static/CACHE/js/output.3a42bfc02f19.js"></script>
        

        <script src="/static/CACHE/js/output.d5f4ec83cdc0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Dominicw/files/home/Dominicw/app.py",
          check_hash: "/user/Dominicw/files/home/Dominicw/app.py",
          update_editor_mode_preference: "/user/Dominicw/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Dominicw/consoles/",
        });
        var filename = "/home/Dominicw/app.py";
        var hash = "a979261677655208c54fc715dbd6b012";
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
            csrfToken: "QlDOk6xM0Q7KTWhlZ6r5YKcdnlQ3X6l5ISoUIuOSpdCvQut1dfpnv6MS6Pi6pzm5",
            path: "/home/Dominicw/app.py"
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
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home/Dominicw" target="_parent">Dominicw</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">app.py</span></span>

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
                <input type="hidden" name="csrfmiddlewaretoken" value="QlDOk6xM0Q7KTWhlZ6r5YKcdnlQ3X6l5ISoUIuOSpdCvQut1dfpnv6MS6Pi6pzm5">
                <button type="submit" class="btn-link logout_link">Log out</button>
        </form>
</li>

      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">&quot;&quot;&quot;Keells Super Price Scraper - Main Application&quot;&quot;&quot;
import os
import json
import logging
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

from scraper import KeellsScraper
from sheets import GoogleSheetsManager
from models import ScrapeRun, User
from config import Config

load_dotenv()

# ── App Setup ────────────────────────────────────────────
app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(
    level=logging.INFO,
    format=&#39;%(asctime)s [%(levelname)s] %(message)s&#39;,
    handlers=[
        logging.FileHandler(&#39;scraper.log&#39;),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ── Auth Setup ────────────────────────────────────────────
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = &#39;login&#39;

# Simple in-memory user store (single admin user)
USERS = {}

@login_manager.user_loader
def load_user(user_id):
    for u in USERS.values():
        if u.id == user_id:
            return u
    return None

def init_users():
    &quot;&quot;&quot;Initialize admin user from env or defaults&quot;&quot;&quot;
    admin_user = os.getenv(&#39;ADMIN_USER&#39;, &#39;admin&#39;)
    admin_pass = os.getenv(&#39;ADMIN_PASS&#39;, &#39;keells2024!&#39;)
    u = User(&#39;1&#39;, admin_user, admin_pass)
    USERS[admin_user] = u
    logger.info(f&quot;Admin user &#39;{admin_user}&#39; initialized&quot;)

# ── Scheduler Setup ───────────────────────────────────────
scheduler = BackgroundScheduler(daemon=True)

# ── Routes: Authentication ────────────────────────────────
@app.route(&#39;/login&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])
def login():
    if request.method == &#39;POST&#39;:
        username = request.form.get(&#39;username&#39;, &#39;&#39;)
        password = request.form.get(&#39;password&#39;, &#39;&#39;)
        user = USERS.get(username)
        if user and user.check_password(password):
            login_user(user)
            flash(&#39;Logged in successfully.&#39;, &#39;success&#39;)
            return redirect(url_for(&#39;dashboard&#39;))
        flash(&#39;Invalid username or password.&#39;, &#39;danger&#39;)
    return render_template(&#39;login.html&#39;)

@app.route(&#39;/logout&#39;)
@login_required
def logout():
    logout_user()
    flash(&#39;Logged out.&#39;, &#39;info&#39;)
    return redirect(url_for(&#39;login&#39;))

# ── Routes: Dashboard ─────────────────────────────────────
@app.route(&#39;/&#39;)
@login_required
def dashboard():
    runs = ScrapeRun.get_recent(10)
    next_run = scheduler.get_job(&#39;weekly_scrape&#39;)
    next_run_time = str(next_run.next_run_time) if next_run else &#39;Not scheduled&#39;
    return render_template(&#39;dashboard.html&#39;,
                           runs=runs,
                           next_run=next_run_time,
                           categories=KeellsScraper.CATEGORIES)

# ── Routes: Settings ──────────────────────────────────────
@app.route(&#39;/settings&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])
@login_required
def settings():
    if request.method == &#39;POST&#39;:
        # Save sheet ID, schedule day/time, API creds path
        sheet_id = request.form.get(&#39;sheet_id&#39;, &#39;&#39;).strip()
        schedule_day = request.form.get(&#39;schedule_day&#39;, &#39;monday&#39;)
        schedule_hour = request.form.get(&#39;schedule_hour&#39;, &#39;06&#39;)
        schedule_min = request.form.get(&#39;schedule_min&#39;, &#39;00&#39;)

        creds_file = request.form.get(&#39;creds_file&#39;, &#39;&#39;).strip()

        config_data = {
            &#39;sheet_id&#39;: sheet_id,
            &#39;schedule_day&#39;: schedule_day,
            &#39;schedule_hour&#39;: int(schedule_hour),
            &#39;schedule_min&#39;: int(schedule_min),
            &#39;creds_file&#39;: creds_file,
            &#39;updated_at&#39;: datetime.now().isoformat()
        }

        with open(&#39;config.json&#39;, &#39;w&#39;) as f:
            json.dump(config_data, f, indent=2)

        # Re-schedule the weekly job
        schedule_weekly_scrape(schedule_day, int(schedule_hour), int(schedule_min))
        flash(&#39;Settings saved and schedule updated.&#39;, &#39;success&#39;)
        return redirect(url_for(&#39;settings&#39;))

    # Load current config
    config_data = load_config()
    return render_template(&#39;settings.html&#39;, config=config_data)

# ── Routes: Manual Trigger ────────────────────────────────
@app.route(&#39;/run-scrape&#39;, methods=[&#39;POST&#39;])
@login_required
def run_scrape():
    &quot;&quot;&quot;Manually trigger a scrape&quot;&quot;&quot;
    config_data = load_config()
    if not config_data.get(&#39;sheet_id&#39;):
        return jsonify({&#39;error&#39;: &#39;Google Sheet ID not configured. Please set it in Settings first.&#39;}), 400

    try:
        run_id = execute_scrape(config_data)
        return jsonify({&#39;success&#39;: True, &#39;run_id&#39;: run_id, &#39;message&#39;: &#39;Scrape completed successfully&#39;})
    except Exception as e:
        logger.exception(&quot;Manual scrape failed&quot;)
        return jsonify({&#39;error&#39;: str(e)}), 500

# ── Routes: Run Detail ────────────────────────────────────
@app.route(&#39;/run/&lt;run_id&gt;&#39;)
@login_required
def run_detail(run_id):
    run = ScrapeRun.get(run_id)
    if not run:
        flash(&#39;Run not found.&#39;, &#39;danger&#39;)
        return redirect(url_for(&#39;dashboard&#39;))
    return render_template(&#39;run_detail.html&#39;, run=run)

# ── Routes: API Status ────────────────────────────────────
@app.route(&#39;/api/status&#39;)
@login_required
def api_status():
    &quot;&quot;&quot;JSON status endpoint&quot;&quot;&quot;
    config_data = load_config()
    next_run = scheduler.get_job(&#39;weekly_scrape&#39;)
    return jsonify({
        &#39;google_sheet_configured&#39;: bool(config_data.get(&#39;sheet_id&#39;)),
        &#39;next_scheduled_run&#39;: str(next_run.next_run_time) if next_run else None,
        &#39;last_runs&#39;: [r.to_dict() for r in ScrapeRun.get_recent(5)]
    })

# ── Core: Execute Scrape ──────────────────────────────────
def execute_scrape(config_data):
    &quot;&quot;&quot;Run the full scrape → Google Sheets pipeline&quot;&quot;&quot;
    run = ScrapeRun.create()
    logger.info(f&quot;Starting scrape run {run.id}&quot;)

    try:
        # 1. Scrape all categories
        scraper = KeellsScraper()
        all_products = []
        category_stats = {}

        for cat_slug, cat_name in KeellsScraper.CATEGORIES.items():
            try:
                products = scraper.scrape_category(cat_slug)
                for p in products:
                    p[&#39;category&#39;] = cat_name
                all_products.extend(products)
                category_stats[cat_name] = {&#39;found&#39;: len(products), &#39;status&#39;: &#39;success&#39;}
                logger.info(f&quot;  Category &#39;{cat_name}&#39;: {len(products)} products&quot;)
            except Exception as e:
                category_stats[cat_name] = {&#39;found&#39;: 0, &#39;status&#39;: f&#39;error: {e}&#39;}
                logger.error(f&quot;  Category &#39;{cat_name}&#39; failed: {e}&quot;)

        run.total_products = len(all_products)
        run.category_stats = category_stats

        # 2. Push to Google Sheets
        sheet_id = config_data.get(&#39;sheet_id&#39;)
        creds_file = config_data.get(&#39;creds_file&#39;, &#39;credentials.json&#39;)

        if sheet_id:
            sheets_mgr = GoogleSheetsManager(creds_file)
            week_label = run.week_label
            sheets_mgr.append_weekly_data(sheet_id, all_products, week_label)
            run.sheet_updated = True
            logger.info(f&quot;  Sheet updated with {len(all_products)} products for {week_label}&quot;)
        else:
            run.sheet_updated = False
            logger.warning(&quot;  No sheet ID configured, skipping Google Sheets update&quot;)

        run.complete(success=True)
        logger.info(f&quot;Scrape run {run.id} completed: {len(all_products)} products&quot;)

    except Exception as e:
        run.complete(success=False, error=str(e))
        logger.exception(f&quot;Scrape run {run.id} failed&quot;)
        raise

    return run.id

# ── Scheduling ─────────────────────────────────────────────
def schedule_weekly_scrape(day=&#39;monday&#39;, hour=6, minute=0):
    &quot;&quot;&quot;Schedule (or re-schedule) the weekly scrape&quot;&quot;&quot;
    days_map = {
        &#39;monday&#39;: 0, &#39;tuesday&#39;: 1, &#39;wednesday&#39;: 2,
        &#39;thursday&#39;: 3, &#39;friday&#39;: 4, &#39;saturday&#39;: 5, &#39;sunday&#39;: 6
    }
    day_num = days_map.get(day.lower(), 0)

    # Remove existing job if any
    existing = scheduler.get_job(&#39;weekly_scrape&#39;)
    if existing:
        scheduler.remove_job(&#39;weekly_scrape&#39;)
        logger.info(&quot;Removed existing scheduled job&quot;)

    scheduler.add_job(
        func=scheduled_scrape_wrapper,
        trigger=&#39;cron&#39;,
        id=&#39;weekly_scrape&#39;,
        day_of_week=day_num,
        hour=hour,
        minute=minute,
        replace_existing=True
    )
    logger.info(f&quot;Weekly scrape scheduled: every {day.capitalize()} at {hour:02d}:{minute:02d}&quot;)

def scheduled_scrape_wrapper():
    &quot;&quot;&quot;Wrapper called by the scheduler&quot;&quot;&quot;
    logger.info(&quot;Scheduled weekly scrape triggered&quot;)
    config_data = load_config()
    if config_data.get(&#39;sheet_id&#39;):
        try:
            execute_scrape(config_data)
        except Exception as e:
            logger.error(f&quot;Scheduled scrape failed: {e}&quot;)
    else:
        logger.warning(&quot;Scheduled scrape skipped: no sheet ID configured&quot;)

# ── Config Helpers ─────────────────────────────────────────
def load_config():
    &quot;&quot;&quot;Load config from config.json with defaults&quot;&quot;&quot;
    defaults = {
        &#39;sheet_id&#39;: &#39;&#39;,
        &#39;schedule_day&#39;: &#39;monday&#39;,
        &#39;schedule_hour&#39;: 6,
        &#39;schedule_min&#39;: 0,
        &#39;creds_file&#39;: &#39;credentials.json&#39;
    }
    try:
        with open(&#39;config.json&#39;, &#39;r&#39;) as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults

# ── Startup ────────────────────────────────────────────────
def init_scheduler():
    &quot;&quot;&quot;Start scheduler with saved config&quot;&quot;&quot;
    config = load_config()
    schedule_weekly_scrape(
        config.get(&#39;schedule_day&#39;, &#39;monday&#39;),
        config.get(&#39;schedule_hour&#39;, 6),
        config.get(&#39;schedule_min&#39;, 0)
    )
    scheduler.start()
    logger.info(&quot;Scheduler started&quot;)

# ── Main ───────────────────────────────────────────────────
if __name__ == &#39;__main__&#39;:
    init_users()
    init_scheduler()
    app.run(host=&#39;0.0.0.0&#39;, port=5000, debug=False)
else:
    # When running via gunicorn
    init_users()
    init_scheduler()</div>
      

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
