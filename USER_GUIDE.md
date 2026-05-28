# 🛒 Keells Super Price Scraper — Complete User Guide

> **What this does:** Scrapes product prices from keellssuper.com every week and populates a Google Sheet for week-by-week price tracking.

---

## Quick Navigation

- [System Overview](#system-overview)
- [Prerequisites Checklist](#prerequisites-checklist)
- [Section 1: Google Cloud Setup (One-Time)](#section-1-google-cloud-setup)
- [Section 2: Deploying to Your Cloudways Server](#section-2-deploying-to-cloudways)
- [Section 3: Google OAuth Authorization (One-Time)](#section-3-google-oauth-authorization)
- [Section 4: Using the Web Dashboard](#section-4-using-the-web-dashboard)
- [Section 5: Your Google Sheet Explained](#section-5-your-google-sheet)
- [Section 6: Ongoing Operations](#section-6-ongoing-operations)
- [Section 7: Maintenance & Troubleshooting](#section-7-maintenance)
- [Section 8: Expanding Categories](#section-8-expanding-categories)
- [Quick Reference Card](#quick-reference-card)

---

## System Overview

```
┌──────────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  keellssuper.com     │────▶│  Python Scraper   │────▶│  Google Sheets   │
│  (10 categories)     │     │  (Flask on Server) │     │  (Your Sheet)    │
└──────────────────────┘     └───────────────────┘     └──────────────────┘
                                      │
                                      │ Web Dashboard (http://IP:5000)
                                      ▼
                             ┌───────────────────┐
                             │  Login → Dashboard │
                             │  Run Now | History │
                             │  Settings | Logs   │
                             └───────────────────┘
```

**Every Monday at 6 AM (default):** The app scrapes all products, creates a new week column in your Google Sheet, and populates every product's current price. You can check results anytime via the web dashboard.

---

## Prerequisites Checklist

Before starting, make sure you have:

| # | What You Need | How to Get It |
|---|--------------|---------------|
| ☐ | A Google/Gmail account | You already have one |
| ☐ | Cloudways server IP + SSH login | From your Cloudways dashboard |
| ☐ | A blank Google Sheet | Go to sheets.google.com → Blank |
| ☐ | SSH client | Built-in on Mac/Linux terminal; PuTTY on Windows |
| ☐ | SCP client (to upload files) | Built-in on Mac/Linux; WinSCP on Windows |
| ☐ | ~30 minutes for initial setup | One time only |

---

## Section 1: Google Cloud Setup

> This creates the security keys so the app can write to your Google Sheet. Do this once.

### 1A: Create Project

1. Go to **https://console.cloud.google.com/**
2. Click the project selector (top-left dropdown) → **NEW PROJECT**
3. Name: `keells-scraper` → **CREATE**
4. Wait for it to be created, then verify it's selected in the dropdown

### 1B: Enable APIs

1. Left menu → **APIs & Services → Library**
2. Search **"Google Sheets API"** → Click → **ENABLE**
3. Go back to Library
4. Search **"Google Drive API"** → Click → **ENABLE**

### 1C: OAuth Consent Screen

1. Left menu → **APIs & Services → OAuth Consent Screen**
2. User Type: **External** → **CREATE**
3. Fill in:
   - App name: `Keells Price Scraper`
   - User support email: your email
   - Developer contact: your email
   - Click **SAVE AND CONTINUE**
4. Scopes page → **ADD OR REMOVE SCOPES** → Search `spreadsheets` → Check `.../auth/spreadsheets` → **UPDATE** → **SAVE AND CONTINUE**
5. Test users → **ADD USERS** → enter your email → **ADD** → **SAVE AND CONTINUE**

### 1D: Create OAuth Client ID

1. Left menu → **APIs & Services → Credentials**
2. **CREATE CREDENTIALS → OAuth Client ID**
3. Application type: **Desktop Application**
4. Name: `Keells Scraper Desktop` → **CREATE**
5. Click **DOWNLOAD JSON** on the popup
6. **Rename** the downloaded file to exactly `credentials.json`
7. Save this file — you'll upload it to the server in Section 2

### 1E: Get Your Google Sheet ID

1. Open your Google Sheet in browser
2. Look at the URL:
   ```
   https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMzOo8i3jHdGZnP8LiKjJq6kH0nG_vY/edit
   ```
3. Copy the part between `/d/` and `/edit` — that's your **Sheet ID**
4. Save it — you'll enter it in the Settings page later

---

## Section 2: Deploying to Cloudways

### 2A: Upload the App Files

**On Mac/Linux terminal:**
```bash
# From wherever you have the keells-scraper folder
scp -r keells-scraper/ master@YOUR_SERVER_IP:/home/master/applications/
```

**On Windows (using WinSCP):**
- Open WinSCP → connect to your server (host: YOUR_SERVER_IP, user: master, password: your password)
- On the left pane, navigate to your `keells-scraper` folder
- On the right pane, navigate to `/home/master/applications/`
- Drag the entire `keells-scraper` folder from left to right

### 2B: Upload credentials.json

Also upload your `credentials.json` into the app folder:

**Mac/Linux:**
```bash
scp credentials.json master@YOUR_SERVER_IP:/home/master/applications/keells-scraper/
```

**Windows (WinSCP):** Drag `credentials.json` into `/home/master/applications/keells-scraper/` on the server

### 2C: SSH into Your Server

```bash
ssh master@YOUR_SERVER_IP
```
Enter your password. You're now on the server.

### 2D: Run the Deployment Script

```bash
cd /home/master/applications/keells-scraper
chmod +x deploy.sh
./deploy.sh
```

This installs everything automatically:
- System libraries for HTML parsing
- Python virtual environment
- All Python packages
- Supervisor (keeps app running 24/7)
- Weekly cron job (backup scheduler)

If the script succeeds, you'll see: **"Deployment Complete!"**

### 2E: Verify It's Running

```bash
sudo supervisorctl status keells-scraper
```

Expected: `keells-scraper    RUNNING    pid 12345, uptime 0:00:15`

### 2F: Access the Web UI

Open your browser:
```
http://YOUR_SERVER_IP:5000
```

You should see a **Login page** with a blue-green gradient background.

---

## Section 3: Google OAuth Authorization

> The app needs permission to write to your sheet. This happens once.

### 3A: Run the Auth Wizard

Still on your server SSH session:
```bash
cd /home/master/applications/keells-scraper
source venv/bin/activate
python3 -c "from sheets import GoogleSheetsManager; m = GoogleSheetsManager(); m.client"
```

You'll see:
```
============================================================
GOOGLE SHEETS AUTHORIZATION REQUIRED
============================================================

Visit this URL to authorize the app:

https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=...&...
```

### 3B: Authorize in Browser

1. **Copy the entire URL** (triple-click to select the whole line)
2. **Paste into your browser** on your local computer
3. Sign in with your Google account
4. Google will warn: "This app isn't verified" → Click **Advanced** → **Go to Keells Price Scraper (unsafe)**
5. Click **Continue** to grant permissions
6. You'll get a long **authorization code** — copy it

### 3C: Complete Authorization

Back in SSH, paste the code:
```
Enter the authorization code: [PASTE HERE]
```

You'll see: `OAuth token saved to token.pickle` ✅

### 3D: Share Your Google Sheet

Last authorization step — give the app edit access:

1. Open your Google Sheet in a browser
2. Click the green **Share** button (top-right)
3. Enter **your own email** (the one you authorized with)
4. Permission: **Editor**
5. Click **Send**

The app can now read and write to your sheet!

---

## Section 4: Using the Web Dashboard

### 4.1 Login

Go to `http://YOUR_SERVER_IP:5000`

| Field | Default Value | How to Change |
|-------|--------------|---------------|
| Username | `admin` | Set `ADMIN_USER` in `.env` file |
| Password | `keells2024!` | Set `ADMIN_PASS` in `.env` file |

### 4.2 Dashboard Page

After login, you see the main dashboard:

```
┌──────────────────────────────────────────────────────────────┐
│  📊 Dashboard                                                │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  ┌─────────┐  │
│  │   5      │  │   10     │  │Mon 6:00 AM   │  │ SUCCESS │  │
│  │Past Runs │  │Categories│  │  Next Run    │  │ Status  │  │
│  └──────────┘  └──────────┘  └──────────────┘  └─────────┘  │
│                                                              │
│  ⚡ Manual Trigger                                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ [▶ Run Scrape Now]  ◌  ✅ Success! ...              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  📋 Run History                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Week                  │Status│Started │Dur  │Products│   │
│  │ 2026-W22 (Jun 1-7)   │✅    │Jun 1   │2:15 │ 1,247  │   │
│  │ 2026-W21 (May 25-31) │✅    │May 25  │1:58 │ 1,203  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  🏷️ Tracked: Fruits Vegetables Meat Seafood Rice Oils ...   │
└──────────────────────────────────────────────────────────────┘
```

**Actions on Dashboard:**
- **"Run Scrape Now"** — immediately scrapes prices and updates your sheet
- **"Details"** on any run row — shows per-category breakdown
- Status badges: green = success, red = failed

### 4.3 Settings Page

Click **Settings** in the top nav bar to configure:

| Setting | What It Is | Example |
|---------|-----------|---------|
| **Google Spreadsheet ID** | The ID from your sheet URL | `1BxiMVs0XRA5nFMzOo8i3jHdGZnP8LiKjJq6kH0nG_vY` |
| **OAuth Credentials File** | Path to credentials.json | `credentials.json` |
| **Schedule Day** | Day of week to run | Monday, Tuesday, etc. |
| **Schedule Hour** | Hour in 24h format | 06 = 6 AM, 14 = 2 PM |
| **Schedule Minute** | Minute of the hour | 00, 15, 30, 45 |

Click **💾 Save Settings** to apply. The schedule updates immediately.

The Settings page also contains a **step-by-step Google OAuth setup guide** (same as Section 1 above).

### 4.4 Run Detail Page

Click **Details** on any run to see:

- Exact start and finish times
- Total duration
- Per-category stats (how many products in each, which failed)
- Whether the Google Sheet was updated
- Full error message if anything went wrong

### 4.5 Logout

Click **Logout** in the top-right corner.

---

## Section 5: Your Google Sheet

### After First Run

Your sheet will have a tab called **"Price Data"**:

| Product Name | Unit | 2026-W22 (Jun 1 - Jun 7) |
|-------------|------|--------------------------|
| Apple Red | 1kg | Rs. 450.00 |
| Banana | 1kg | Rs. 280.00 |
| Chicken Breast | 500g | Rs. 620.00 |
| ... | ... | ... |

### After Second Week

A new column is added:

| Product Name | Unit | 2026-W22 (Jun 1-7) | 2026-W23 (Jun 8-14) |
|-------------|------|---------------------|---------------------|
| Apple Red | 1kg | Rs. 450.00 | Rs. 455.00 |
| Banana | 1kg | Rs. 280.00 | Rs. 275.00 |
| Chicken Breast | 500g | Rs. 620.00 | Rs. 640.00 |
| New Product XYZ | 200g | — | Rs. 150.00 |

**How it works:**
- Products are **matched by name** across weeks (case-insensitive)
- Existing products get their price filled into the new column
- New products (not in previous weeks) get new rows at the bottom
- Each week adds exactly one column
- Duplicate weeks are skipped — safe to run multiple times

### You Can Customize

- Add your own columns, formulas, charts
- Add conditional formatting (e.g., highlight price increases in red)
- The app only writes to its price columns — won't touch your additions
- Create a chart comparing price trends over multiple weeks

---

## Section 6: Ongoing Operations

### Normal Weekly Flow (Automatic)

You don't need to do anything. Every week:

1. The scheduler triggers at your chosen day/time
2. All 10 categories are scraped from keellssuper.com
3. Your Google Sheet gets a new column
4. All prices are populated
5. The run is logged in the dashboard

### Checking Status Anytime

Visit `http://YOUR_SERVER_IP:5000` → see recent runs and their statuses.

### Running a Manual Scrape

Dashboard → click **"Run Scrape Now"** → wait ~2 minutes → page refreshes with results.

### Changing Schedule

Settings → pick new day/time → Save Settings → done.

### Changing the Admin Password

On your server via SSH:
```bash
cd /home/master/applications/keells-scraper
nano .env
# Change ADMIN_USER and ADMIN_PASS
# Save (Ctrl+O, Enter, Ctrl+X)

sudo supervisorctl restart keells-scraper
```

---

## Section 7: Maintenance

### Viewing Logs

SSH into server, then:

```bash
# Scraping activity log (what was scraped, errors)
tail -100 /home/master/applications/keells-scraper/scraper.log

# Web access log (who visited)
tail -100 /home/master/applications/keells-scraper/access.log

# Application errors
tail -100 /home/master/applications/keells-scraper/error.log
```

### Restarting the App

```bash
sudo supervisorctl restart keells-scraper
```

### App Status

```bash
sudo supervisorctl status keells-scraper
```

### Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| **"Sheet ID not configured"** | Not entered yet | Go to Settings → paste Sheet ID |
| **"credentials.json not found"** | File not on server | Upload credentials.json to `/home/master/applications/keells-scraper/` |
| **0 products / empty results** | Site structure changed | Check scraper.log; may need updates |
| **Sheet not updating** | Token expired or sheet not shared | Delete token.pickle and re-run Section 3; re-share sheet |
| **401 / token error** | Refresh token invalid | `rm /home/master/applications/keells-scraper/token.pickle` then re-run Section 3 |
| **502 Bad Gateway in browser** | Gunicorn crashed | `sudo supervisorctl restart keells-scraper` |
| **Some categories show 0** | URL slug doesn't match | Check keellssuper.com for that category's URL; update in scraper.py |
| **Memory usage high** | Too many workers | Edit gunicorn_config.py → workers = 1 |

### Updating the App Code

When you make changes to the scraper:
```bash
# Upload updated files
scp -r keells-scraper/*.py master@YOUR_SERVER_IP:/home/master/applications/keells-scraper/
scp -r keells-scraper/templates/ master@YOUR_SERVER_IP:/home/master/applications/keells-scraper/

# Restart
ssh master@YOUR_SERVER_IP "sudo supervisorctl restart keells-scraper"
```

---

## Section 8: Expanding Categories

Currently tracked: **Fruits, Vegetables, Meat & Poultry, Seafood, Rice & Pulses, Oils & Fats, Spices & Condiments, Canned & Tinned, Beverages** (9 categories active).

To add more:

1. Edit `scraper.py` on your local machine
2. Find the `CATEGORIES` dictionary (around line 28)
3. Uncomment or add new entries:
   ```python
   CATEGORIES = {
       'fruits':            'Fruits',
       'vegetables':        'Vegetables',
       # ... existing ...
       'dairy':             'Dairy',             # Uncomment to add
       'bakery':            'Bakery',             # Uncomment to add
       'personal-care':     'Personal Care',      # Add new line
   }
   ```
4. The category key (left side) should match the URL slug on keellssuper.com
5. Upload the updated scraper.py to the server and restart

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│  KEELLS PRICE SCRAPER — QUICK REFERENCE                    │
├─────────────────────────────────────────────────────────────┤
│  Web Dashboard:    http://YOUR_SERVER_IP:5000              │
│  Default Login:    admin / keells2024!                     │
│                                                            │
│  Server Directory: /home/master/applications/keells-scraper│
│  Config:           config.json (auto-created via Settings) │
│  OAuth Creds:      credentials.json (you upload)           │
│  OAuth Token:      token.pickle (auto-created)             │
│  Logs:             scraper.log, access.log, error.log      │
│                                                            │
│  Restart App:      sudo supervisorctl restart keells-scraper│
│  Check Status:     sudo supervisorctl status keells-scraper │
│  View Logs:        tail -100 scraper.log                   │
│                                                            │
│  Google Cloud:     https://console.cloud.google.com/       │
│  Create Sheet:     https://sheets.google.com/              │
├─────────────────────────────────────────────────────────────┤
│  FLOW:                                                      │
│  1. Google Cloud → credentials.json → upload to server      │
│  2. deploy.sh → installs everything                         │
│  3. python3 -c "..." → OAuth one-time authorization         │
│  4. Share Google Sheet (Editor) with your email             │
│  5. Web UI → Settings → paste Sheet ID + set schedule       │
│  6. Dashboard → "Run Scrape Now" → check your Sheet!        │
└─────────────────────────────────────────────────────────────┘