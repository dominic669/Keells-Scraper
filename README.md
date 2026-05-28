# 🛒 Keells Super Price Scraper

Automated weekly price scraper for [keellssuper.com](https://keellssuper.com) that tracks product prices across multiple categories and pushes data to Google Sheets for week-by-week price comparison.

## Features

- **Multi-strategy scraping**: Attempts API endpoints first, falls back to HTML parsing
- **10 product categories**: Fruits, Vegetables, Meat, Seafood, Rice/Pulses, Oils, Spices, Canned Food, Beverages
- **Google Sheets integration**: OAuth 2.0 authenticated, writes prices to a single sheet with week-by-week columns
- **Weekly scheduling**: Runs automatically via APScheduler + backup cron job
- **Web dashboard**: Login-protected interface to view run history, trigger manual scrapes, and configure settings
- **Lightweight**: ~50MB RAM idle, single gunicorn worker — designed for 2GB Cloudways servers

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3 + Flask |
| Scraping | BeautifulSoup4 + lxml + requests |
| Google Sheets | gspread + google-auth-oauthlib |
| Scheduling | APScheduler (in-app) + cron (backup) |
| Process Manager | Supervisor + Gunicorn |
| Web UI | Jinja2 templates (vanilla HTML/CSS/JS, no framework) |

## Quick Start

### Prerequisites

- Python 3.9+
- A Google Cloud project with Sheets API and Drive API enabled
- OAuth 2.0 Client ID (Desktop Application type) → `credentials.json`
- A Google Sheet you own (or have edit access to)

### Local Setup

```bash
# 1. Clone / copy the project
cd keells-scraper

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and configure environment
cp .env.example .env
# Edit .env with your SECRET_KEY, ADMIN_USER, ADMIN_PASS

# 5. Run the app
python app.py
# App starts at http://localhost:5000
```

### First Google OAuth Authorization

The app uses a console-based OAuth flow (works on headless servers):

```bash
cd keells-scraper
source venv/bin/activate
python3 -c "from sheets import GoogleSheetsManager; m = GoogleSheetsManager(); m.client"
```

This will:
1. Print a Google authorization URL
2. You visit it in your browser, sign in, get a code
3. Paste the code back in the terminal
4. The refresh token is saved as `token.pickle` (used for all future automated runs)

### Configure via Web UI

1. Visit `http://your-server:5000`
2. Login with default credentials (`admin` / `keells2024!`)
3. Go to **Settings** and enter your Google Spreadsheet ID
4. Set your preferred schedule (default: Monday 6 AM)
5. Click **"Run Scrape Now"** from the Dashboard to test

## Sheet Structure

The Google Sheet uses a **single sheet** with week-by-week columns:

| Product Name | Unit | 2026-W21 (May 25 - May 31) | 2026-W22 (Jun 1 - Jun 7) | ... |
|-------------|------|---------------------------|--------------------------|-----|
| Apple | 1kg | Rs. 450.00 | Rs. 455.00 | |
| Banana | 1kg | Rs. 280.00 | Rs. 275.00 | |
| Chicken Breast | 500g | Rs. 620.00 | Rs. 640.00 | |

- **New products** automatically get new rows
- **Existing products** are matched by name and prices fill into new week columns
- **Each week** adds one new column (no duplicate weeks)

## Deployment on Cloudways

### Upload files to server

```bash
# From your local machine
scp -r keells-scraper/ master@YOUR_SERVER_IP:/home/master/applications/
```

### SSH into server and run deploy script

```bash
ssh master@YOUR_SERVER_IP
cd /home/master/applications/keells-scraper
chmod +x deploy.sh
./deploy.sh
```

### Manual deployment (if deploy.sh doesn't work)

```bash
ssh master@YOUR_SERVER_IP

# Create app directory
mkdir -p /home/master/applications/keells-scraper
cd /home/master/applications/keells-scraper

# Setup venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start with gunicorn (test first)
gunicorn --bind 0.0.0.0:5000 app:app

# Set up Supervisor for persistence
sudo nano /etc/supervisor/conf.d/keells-scraper.conf
# (paste the supervisor config from deploy.sh)
sudo supervisorctl reread
sudo supervisorctl update
```

### Set up cron as backup

```bash
crontab -e
# Add:
0 6 * * 1 cd /home/master/applications/keells-scraper && /home/master/applications/keells-scraper/venv/bin/python3 -c "from app import load_config, execute_scrape; import logging; logging.basicConfig(level=logging.INFO); config=load_config(); config.get('sheet_id') and execute_scrape(config)" >> /home/master/applications/keells-scraper/cron.log 2>&1
```

## Adding More Categories

Edit `scraper.py` → `CATEGORIES` dictionary. Uncomment or add new entries:

```python
CATEGORIES = {
    # ... existing categories ...
    'dairy':         'Dairy',            # Uncommented → now tracked
    'household-cleaning': 'Household',   # New category → must match URL slug
}
```

The scraper will auto-discover the correct URL pattern for each category.

## Security Notes

- **Change default credentials**: Set `ADMIN_USER` and `ADMIN_PASS` in `.env` or environment variables
- **Use HTTPS**: Put the app behind Nginx/Apache reverse proxy with SSL
- **Firewall**: Restrict port 5000 to localhost only, access via reverse proxy
- **OAuth credentials**: Never commit `credentials.json` or `token.pickle` (they're in `.gitignore`)

## File Structure

```
keells-scraper/
├── app.py                  # Flask application (routes, scheduler, main logic)
├── scraper.py              # KeellsSuper website scraper (HTML + API strategies)
├── sheets.py               # Google Sheets OAuth + read/write operations
├── models.py               # User and ScrapeRun data models
├── config.py               # App configuration
├── gunicorn_config.py      # Production server config (lightweight, 1 worker)
├── deploy.sh               # Cloudways deployment script
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Ignored files
├── templates/              # Web UI templates
│   ├── base.html           # Base layout with nav, styles
│   ├── login.html          # Login page
│   ├── dashboard.html      # Main dashboard with stats, run history, manual trigger
│   ├── settings.html       # Configuration page + OAuth setup guide
│   └── run_detail.html     # Detailed view of a single scrape run
├── data/                   # Scrape run JSON files (auto-created)
├── credentials.json        # Google OAuth client secret (YOU provide this)
├── token.pickle            # OAuth refresh token (auto-generated)
├── config.json             # App settings (auto-created via web UI)
└── scraper.log             # Application logs
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "credentials.json not found" | Download OAuth client JSON from Google Cloud Console |
| "Token has expired" / 401 errors | Delete `token.pickle` and re-authorize |
| Empty product results | Check keellssuper.com is accessible; category URLs may have changed |
| "Sheet not found" | Share the Google Sheet with your OAuth email (Editor access) |
| Memory usage too high | Reduce `workers` in gunicorn_config.py (1 worker = ~50MB) |
| Scrape takes too long | Increase `timeout` in gunicorn; reduce categories |