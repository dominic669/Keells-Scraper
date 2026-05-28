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
        <title>config.py : /home/Dominicw/config.py : Editor : Dominicw : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="config.py : /home/Dominicw/config.py : Editor : Dominicw : PythonAnywhere">
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
            Anywhere.csrfToken = "V320KS3F3fctlduZK3vWwIP70vdgpT58NAN68gkLsCHeiLGFYcte34pMJZFjRm68";
        </script>
        <script src="/static/CACHE/js/output.3a42bfc02f19.js"></script>
        

        <script src="/static/CACHE/js/output.d5f4ec83cdc0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Dominicw/files/home/Dominicw/config.py",
          check_hash: "/user/Dominicw/files/home/Dominicw/config.py",
          update_editor_mode_preference: "/user/Dominicw/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Dominicw/consoles/",
        });
        var filename = "/home/Dominicw/config.py";
        var hash = "e6d577ea94ec415df5d14a0e6af7cb3a";
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
            csrfToken: "V320KS3F3fctlduZK3vWwIP70vdgpT58NAN68gkLsCHeiLGFYcte34pMJZFjRm68",
            path: "/home/Dominicw/config.py"
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
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Dominicw/files/home/Dominicw" target="_parent">Dominicw</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">config.py</span></span>

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
                <input type="hidden" name="csrfmiddlewaretoken" value="V320KS3F3fctlduZK3vWwIP70vdgpT58NAN68gkLsCHeiLGFYcte34pMJZFjRm68">
                <button type="submit" class="btn-link logout_link">Log out</button>
        </form>
</li>

      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">&quot;&quot;&quot;Application Configuration&quot;&quot;&quot;
import os


class Config:
    SECRET_KEY = os.getenv(&#39;SECRET_KEY&#39;, &#39;change-this-to-a-random-secret-key-in-production&#39;)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = &#39;Lax&#39;
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

    # Scraper settings
    REQUEST_TIMEOUT = 30  # seconds
    REQUEST_DELAY = 0.5   # seconds between requests (be polite)
    MAX_RETRIES = 3</div>
      

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
