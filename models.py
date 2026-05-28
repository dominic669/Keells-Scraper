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
        <title>models.py : /home/Dominicw/models.py : Editor : Dominicw : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="models.py : /home/Dominicw/models.py : Editor : Dominicw : PythonAnywhere">
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
            Anywhere.csrfToken = "HQzOgM90s66vcTf8wnMlSvHgqqDtZn4tznkUEaq6RtBg9rrOKwKDpRhV9U5wrQ5t";
        </script>
        <script src="/static/CACHE/js/output.3a42bfc02f19.js"></script>
        

        <script src="/static/CACHE/js/output.d5f4ec83cdc0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Dominicw/files/home/Dominicw/models.py",
          check_hash: "/user/Dominicw/files/home/Dominicw/models.py",
          update_editor_mode_preference: "/user/Dominicw/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Dominicw/consoles/",
        });
        var filename = "/home/Dominicw/models.py";
        var hash = "bdf47fde61a99fefb5f723d4b0f4ae1b";
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
            csrfToken: "HQzOgM90s66vcTf8wnMlSvHgqqDtZn4tznkUEaq6RtBg9rrOKwKDpRhV9U5wrQ5t",
            path: "/home/Dominicw/models.py"
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
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home/Dominicw" target="_parent">Dominicw</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">models.py</span></span>

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
                <input type="hidden" name="csrfmiddlewaretoken" value="HQzOgM90s66vcTf8wnMlSvHgqqDtZn4tznkUEaq6RtBg9rrOKwKDpRhV9U5wrQ5t">
                <button type="submit" class="btn-link logout_link">Log out</button>
        </form>
</li>

      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">&quot;&quot;&quot;Data models for the Keells scraper app&quot;&quot;&quot;
import json
import os
import uuid
import hashlib
from datetime import datetime, timedelta
from flask_login import UserMixin

DATA_DIR = &#39;data&#39;


class User(UserMixin):
    &quot;&quot;&quot;Simple admin user for web interface login&quot;&quot;&quot;

    def __init__(self, user_id, username, password_hash):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash if len(password_hash) == 64 else hashlib.sha256(password_hash.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


class ScrapeRun:
    &quot;&quot;&quot;Represents a single scrape execution&quot;&quot;&quot;

    def __init__(self, run_id, week_label, status, started_at, finished_at,
                 total_products, category_stats, sheet_updated, error):
        self.id = run_id
        self.week_label = week_label
        self.status = status  # &#39;running&#39;, &#39;success&#39;, &#39;failed&#39;
        self.started_at = started_at
        self.finished_at = finished_at
        self.total_products = total_products
        self.category_stats = category_stats or {}
        self.sheet_updated = sheet_updated
        self.error = error

    @property
    def duration(self):
        if self.started_at and self.finished_at:
            delta = datetime.fromisoformat(self.finished_at) - datetime.fromisoformat(self.started_at)
            return str(delta).split(&#39;.&#39;)[0]
        return &#39;N/A&#39;

    @property
    def success_rate(self):
        if not self.category_stats:
            return &#39;N/A&#39;
        total = len(self.category_stats)
        success = sum(1 for v in self.category_stats.values() if v.get(&#39;status&#39;) == &#39;success&#39;)
        return f&quot;{success}/{total}&quot; if total &gt; 0 else &#39;0/0&#39;

    def to_dict(self):
        return {
            &#39;id&#39;: self.id,
            &#39;week_label&#39;: self.week_label,
            &#39;status&#39;: self.status,
            &#39;started_at&#39;: self.started_at,
            &#39;finished_at&#39;: self.finished_at,
            &#39;duration&#39;: self.duration,
            &#39;total_products&#39;: self.total_products,
            &#39;category_stats&#39;: self.category_stats,
            &#39;sheet_updated&#39;: self.sheet_updated,
            &#39;success_rate&#39;: self.success_rate,
            &#39;error&#39;: self.error
        }

    @classmethod
    def create(cls):
        &quot;&quot;&quot;Create a new run record&quot;&quot;&quot;
        os.makedirs(DATA_DIR, exist_ok=True)
        run_id = datetime.now().strftime(&#39;%Y%m%d-%H%M%S-&#39;) + uuid.uuid4().hex[:6]
        week_label = cls._get_week_label()

        run = cls(
            run_id=run_id,
            week_label=week_label,
            status=&#39;running&#39;,
            started_at=datetime.now().isoformat(),
            finished_at=None,
            total_products=0,
            category_stats={},
            sheet_updated=False,
            error=None
        )
        run._save()
        return run

    def complete(self, success=True, error=None):
        &quot;&quot;&quot;Mark run as completed&quot;&quot;&quot;
        self.status = &#39;success&#39; if success else &#39;failed&#39;
        self.finished_at = datetime.now().isoformat()
        self.error = error
        self._save()

    def _save(self):
        &quot;&quot;&quot;Persist run to disk as JSON&quot;&quot;&quot;
        os.makedirs(DATA_DIR, exist_ok=True)
        filepath = os.path.join(DATA_DIR, f&#39;{self.id}.json&#39;)
        with open(filepath, &#39;w&#39;) as f:
            json.dump(self.to_dict(), f, indent=2, default=str)

    @classmethod
    def get(cls, run_id):
        &quot;&quot;&quot;Load a specific run from disk&quot;&quot;&quot;
        filepath = os.path.join(DATA_DIR, f&#39;{run_id}.json&#39;)
        if not os.path.exists(filepath):
            return None
        with open(filepath, &#39;r&#39;) as f:
            data = json.load(f)
        return cls(**data)

    @classmethod
    def get_recent(cls, limit=10):
        &quot;&quot;&quot;Get most recent runs, newest first&quot;&quot;&quot;
        os.makedirs(DATA_DIR, exist_ok=True)
        files = sorted(
            [f for f in os.listdir(DATA_DIR) if f.endswith(&#39;.json&#39;)],
            reverse=True
        )[:limit]

        runs = []
        for fname in files:
            with open(os.path.join(DATA_DIR, fname), &#39;r&#39;) as f:
                data = json.load(f)
        runs.append(cls(
    run_id=data.get(&#39;id&#39;),
    week_label=data.get(&#39;week_label&#39;),
    status=data.get(&#39;status&#39;),
    started_at=data.get(&#39;started_at&#39;),
    finished_at=data.get(&#39;finished_at&#39;),
    total_products=data.get(&#39;total_products&#39;),
    category_stats=data.get(&#39;category_stats&#39;),
    sheet_updated=data.get(&#39;sheet_updated&#39;),
    error=data.get(&#39;error&#39;)
))
        return runs

    @staticmethod
    def _get_week_label():
        &quot;&quot;&quot;Generate a week label like &#39;2026-W22 (May 25 - May 31)&#39;&quot;&quot;&quot;
        now = datetime.now()
        iso = now.isocalendar()
        week_num = iso[1]
        year = iso[0]
        # Monday of this week
        monday = now - timedelta(days=now.weekday())
        sunday = monday + timedelta(days=6)
        return f&quot;{year}-W{week_num:02d} ({monday.strftime(&#39;%b %d&#39;)} - {sunday.strftime(&#39;%b %d&#39;)})&quot;</div>
      

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
