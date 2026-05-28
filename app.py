"""Keells Super Price Scraper - Main Application"""
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
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ── Auth Setup ────────────────────────────────────────────
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simple in-memory user store (single admin user)
USERS = {}

@login_manager.user_loader
def load_user(user_id):
    for u in USERS.values():
        if u.id == user_id:
            return u
    return None

def init_users():
    """Initialize admin user from env or defaults"""
    admin_user = os.getenv('ADMIN_USER', 'admin')
    admin_pass = os.getenv('ADMIN_PASS', 'keells2024!')
    u = User('1', admin_user, admin_pass)
    USERS[admin_user] = u
    logger.info(f"Admin user '{admin_user}' initialized")

# ── Scheduler Setup ───────────────────────────────────────
scheduler = BackgroundScheduler(daemon=True)

# ── Routes: Authentication ────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user = USERS.get(username)
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('login'))

# ── Routes: Dashboard ─────────────────────────────────────
@app.route('/')
@login_required
def dashboard():
    runs = ScrapeRun.get_recent(10)
    next_run = scheduler.get_job('weekly_scrape')
    next_run_time = str(next_run.next_run_time) if next_run else 'Not scheduled'
    return render_template('dashboard.html',
                           runs=runs,
                           next_run=next_run_time,
                           categories=KeellsScraper.CATEGORIES)

# ── Routes: Settings ──────────────────────────────────────
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        # Save sheet ID, schedule day/time, API creds path
        sheet_id = request.form.get('sheet_id', '').strip()
        schedule_day = request.form.get('schedule_day', 'monday')
        schedule_hour = request.form.get('schedule_hour', '06')
        schedule_min = request.form.get('schedule_min', '00')

        creds_file = request.form.get('creds_file', '').strip()

        config_data = {
            'sheet_id': sheet_id,
            'schedule_day': schedule_day,
            'schedule_hour': int(schedule_hour),
            'schedule_min': int(schedule_min),
            'creds_file': creds_file,
            'updated_at': datetime.now().isoformat()
        }

        with open('config.json', 'w') as f:
            json.dump(config_data, f, indent=2)

        # Re-schedule the weekly job
        schedule_weekly_scrape(schedule_day, int(schedule_hour), int(schedule_min))
        flash('Settings saved and schedule updated.', 'success')
        return redirect(url_for('settings'))

    # Load current config
    config_data = load_config()
    return render_template('settings.html', config=config_data)

# ── Routes: Manual Trigger ────────────────────────────────
@app.route('/run-scrape', methods=['POST'])
@login_required
def run_scrape():
    """Manually trigger a scrape"""
    config_data = load_config()
    if not config_data.get('sheet_id'):
        return jsonify({'error': 'Google Sheet ID not configured. Please set it in Settings first.'}), 400

    try:
        run_id = execute_scrape(config_data)
        return jsonify({'success': True, 'run_id': run_id, 'message': 'Scrape completed successfully'})
    except Exception as e:
        logger.exception("Manual scrape failed")
        return jsonify({'error': str(e)}), 500

# ── Routes: Run Detail ────────────────────────────────────
@app.route('/run/<run_id>')
@login_required
def run_detail(run_id):
    run = ScrapeRun.get(run_id)
    if not run:
        flash('Run not found.', 'danger')
        return redirect(url_for('dashboard'))
    return render_template('run_detail.html', run=run)

# ── Routes: API Status ────────────────────────────────────
@app.route('/api/status')
@login_required
def api_status():
    """JSON status endpoint"""
    config_data = load_config()
    next_run = scheduler.get_job('weekly_scrape')
    return jsonify({
        'google_sheet_configured': bool(config_data.get('sheet_id')),
        'next_scheduled_run': str(next_run.next_run_time) if next_run else None,
        'last_runs': [r.to_dict() for r in ScrapeRun.get_recent(5)]
    })

# ── Core: Execute Scrape ──────────────────────────────────
def execute_scrape(config_data):
    """Run the full scrape → Google Sheets pipeline"""
    run = ScrapeRun.create()
    logger.info(f"Starting scrape run {run.id}")

    try:
        # 1. Scrape all categories
        scraper = KeellsScraper()
        all_products = []
        category_stats = {}

        for cat_slug, cat_name in KeellsScraper.CATEGORIES.items():
            try:
                products = scraper.scrape_category(cat_slug)
                for p in products:
                    p['category'] = cat_name
                all_products.extend(products)
                category_stats[cat_name] = {'found': len(products), 'status': 'success'}
                logger.info(f"  Category '{cat_name}': {len(products)} products")
            except Exception as e:
                category_stats[cat_name] = {'found': 0, 'status': f'error: {e}'}
                logger.error(f"  Category '{cat_name}' failed: {e}")

        run.total_products = len(all_products)
        run.category_stats = category_stats

        # 2. Push to Google Sheets
        sheet_id = config_data.get('sheet_id')
        creds_file = config_data.get('creds_file', 'credentials.json')

        if sheet_id:
            sheets_mgr = GoogleSheetsManager(creds_file)
            week_label = run.week_label
            sheets_mgr.append_weekly_data(sheet_id, all_products, week_label)
            run.sheet_updated = True
            logger.info(f"  Sheet updated with {len(all_products)} products for {week_label}")
        else:
            run.sheet_updated = False
            logger.warning("  No sheet ID configured, skipping Google Sheets update")

        run.complete(success=True)
        logger.info(f"Scrape run {run.id} completed: {len(all_products)} products")

    except Exception as e:
        run.complete(success=False, error=str(e))
        logger.exception(f"Scrape run {run.id} failed")
        raise

    return run.id

# ── Scheduling ─────────────────────────────────────────────
def schedule_weekly_scrape(day='monday', hour=6, minute=0):
    """Schedule (or re-schedule) the weekly scrape"""
    days_map = {
        'monday': 0, 'tuesday': 1, 'wednesday': 2,
        'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6
    }
    day_num = days_map.get(day.lower(), 0)

    # Remove existing job if any
    existing = scheduler.get_job('weekly_scrape')
    if existing:
        scheduler.remove_job('weekly_scrape')
        logger.info("Removed existing scheduled job")

    scheduler.add_job(
        func=scheduled_scrape_wrapper,
        trigger='cron',
        id='weekly_scrape',
        day_of_week=day_num,
        hour=hour,
        minute=minute,
        replace_existing=True
    )
    logger.info(f"Weekly scrape scheduled: every {day.capitalize()} at {hour:02d}:{minute:02d}")

def scheduled_scrape_wrapper():
    """Wrapper called by the scheduler"""
    logger.info("Scheduled weekly scrape triggered")
    config_data = load_config()
    if config_data.get('sheet_id'):
        try:
            execute_scrape(config_data)
        except Exception as e:
            logger.error(f"Scheduled scrape failed: {e}")
    else:
        logger.warning("Scheduled scrape skipped: no sheet ID configured")

# ── Config Helpers ─────────────────────────────────────────
def load_config():
    """Load config from config.json with defaults"""
    defaults = {
        'sheet_id': '',
        'schedule_day': 'monday',
        'schedule_hour': 6,
        'schedule_min': 0,
        'creds_file': 'credentials.json'
    }
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults

# ── Startup ────────────────────────────────────────────────
def init_scheduler():
    """Start scheduler with saved config"""
    config = load_config()
    schedule_weekly_scrape(
        config.get('schedule_day', 'monday'),
        config.get('schedule_hour', 6),
        config.get('schedule_min', 0)
    )
    scheduler.start()
    logger.info("Scheduler started")

# ── Main ───────────────────────────────────────────────────
if __name__ == '__main__':
    init_users()
    init_scheduler()
    app.run(host='0.0.0.0', port=5000, debug=False)
else:
    # When running via gunicorn
    init_users()
    init_scheduler()