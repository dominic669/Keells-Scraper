#!/bin/bash
# ─────────────────────────────────────────────────────────────
# Keells Price Scraper - Cloudways Deployment Script
# Run this on your Cloudways server via SSH
#
# Usage: APP_DIR=/home/master/applications/YOUR_APP APP_PORT=5001 ./deploy.sh
# Or edit the variables below before running.
# ─────────────────────────────────────────────────────────────

set -e

# ── CONFIGURE THESE ───────────────────────────────────
# CHANGE THIS to your actual application path on Cloudways
APP_DIR="${APP_DIR:-/home/master/applications/keells-scraper}"

# Port for the web dashboard (must not conflict with other apps)
# Common Cloudways apps use: 80, 443, 8080, 8000, 3000, etc.
# Pick an unused port. 5001 is a safe default.
APP_PORT="${APP_PORT:-5001}"

SUPERVISOR_NAME="keells-scraper"
PYTHON_BIN="python3"
# ───────────────────────────────────────────────────────

echo "========================================="
echo " Keells Price Scraper - Deployment"
echo "========================================="
echo ""
echo " App Directory : $APP_DIR"
echo " Web Port      : $APP_PORT"
echo " Supervisor    : $SUPERVISOR_NAME"
echo ""

# 1. Create app directory
echo "[1/6] Creating app directory..."
mkdir -p "$APP_DIR"
cd "$APP_DIR"

# 2. Install system dependencies (lxml needs libxml2)
echo "[2/6] Installing system dependencies..."
sudo apt-get update -qq
sudo apt-get install -y -qq python3-pip python3-venv libxml2-dev libxslt1-dev 2>&1 | tail -1

# 3. Create virtual environment
echo "[3/6] Setting up Python virtual environment..."
$PYTHON_BIN -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
echo "[4/6] Installing Python packages..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

# 5. Start Gunicorn with Supervisor
echo "[5/6] Configuring process manager (Supervisor)..."

# Create supervisor config
sudo tee "/etc/supervisor/conf.d/${SUPERVISOR_NAME}.conf" > /dev/null <<SUPERVISOR_EOF
[program:${SUPERVISOR_NAME}]
command=${APP_DIR}/venv/bin/gunicorn app:app
    --bind 0.0.0.0:${APP_PORT}
    --workers 1
    --preload
    --timeout 600
    --access-logfile ${APP_DIR}/access.log
    --error-logfile ${APP_DIR}/error.log
    --log-level info
directory=${APP_DIR}
user=master
autostart=true
autorestart=true
stdout_logfile=${APP_DIR}/supervisor.log
stderr_logfile=${APP_DIR}/supervisor_err.log
environment=PYTHONUNBUFFERED="1"
SUPERVISOR_EOF

# Reload supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart "$SUPERVISOR_NAME"

# 6. Set up weekly cron job as backup scheduler
echo "[6/6] Setting up backup cron job..."

CRON_LOG="${APP_DIR}/cron.log"

# Create a small wrapper script for the cron job
CRON_SCRIPT="${APP_DIR}/run_scrape_cron.sh"
cat > "$CRON_SCRIPT" <<CRON_EOF
#!/bin/bash
cd "${APP_DIR}"
source venv/bin/activate
python3 -c "
from app import load_config, execute_scrape
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler('${APP_DIR}/scraper.log'), logging.StreamHandler()]
)
config = load_config()
if config.get('sheet_id'):
    execute_scrape(config)
else:
    print('No sheet_id configured. Skipping.')
"
CRON_EOF
chmod +x "$CRON_SCRIPT"

# Add cron if not exists (runs every Monday at 6 AM)
(crontab -l 2>/dev/null | grep -v "${SUPERVISOR_NAME}"; echo "0 6 * * 1 ${CRON_SCRIPT} >> ${CRON_LOG} 2>&1 # ${SUPERVISOR_NAME} weekly scrape") | crontab -

echo ""
echo "========================================="
echo " Deployment Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo " 1. Upload your Google OAuth credentials.json to: ${APP_DIR}/"
echo " 2. Run the initial OAuth authorization:"
echo "    cd ${APP_DIR} && source venv/bin/activate && python3 -c \"from sheets import GoogleSheetsManager; m = GoogleSheetsManager(); m.client\""
echo " 3. Access the web dashboard at: http://YOUR_SERVER_IP:${APP_PORT}"
echo " 4. Set up your Google Sheet ID in the Settings page"
echo ""
echo "App Directory : ${APP_DIR}"
echo "Web Port      : ${APP_PORT}"
echo "Supervisor    : sudo supervisorctl status ${SUPERVISOR_NAME}"
echo ""
echo "Files:"
echo "  Config  : ${APP_DIR}/config.json"
echo "  Logs    : ${APP_DIR}/scraper.log"
echo "  Data    : ${APP_DIR}/data/"
echo "  Cron log: ${CRON_LOG}"