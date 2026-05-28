# 🚀 Deploying Keells Scraper to Cloudways — Step-by-Step

> **Your Setup**: 3 projects, 3 apps already running. This goes under `worldinflationtracker` as a 2nd application.

---

## Before You Start — Know Your Server

### Step 0: SSH into Cloudways to See Your Current Setup

```bash
ssh master@YOUR_SERVER_IP
```

Once logged in, run these commands to understand your current setup:

```bash
# See all applications (Cloudways stores them here)
ls -la /home/master/applications/

# See what ports are already in use
sudo netstat -tlnp | grep LISTEN

# See existing supervisor processes
sudo supervisorctl status
```

**Write down what you see.** You need to know:
- What folders exist under `/home/master/applications/`
- What ports are taken (e.g., 80, 443, 8080, 3000, 5000, 8000, etc.)
- What supervisor programs are already running

---

## Step 1: Pick Your App Folder Name and Port

On Cloudways, each application is a folder under `/home/master/applications/`.

Since this belongs to your `worldinflationtracker` project, **pick one of these naming conventions:**

| Option | Folder Path | Example |
|--------|------------|---------|
| **A** (simple) | `/home/master/applications/keells-scraper` | Clean, separate |
| **B** (project-prefixed) | `/home/master/applications/worldinflationtracker-keells` | Groups by project |

**Pick an unused port.** Based on what you saw in Step 0, choose a free port:
- If port `5001` is free → use `5001`
- If port `5050` is free → use `5050`
- Avoid: 80, 443, 22, 3306, 8080, 3000 (commonly used)

**Write these down:**
```
APP_FOLDER = /home/master/applications/___________
APP_PORT   = ________
```

---

## Step 2: Upload Files to Cloudways

### Option A: Using SCP (Mac / Linux / WSL)

From your local machine where the `keells-scraper` folder lives:

```bash
# Upload the entire folder to a temp location first
scp -r keells-scraper/ master@YOUR_SERVER_IP:/tmp/keells-scraper/
```

### Option B: Using WinSCP (Windows)

1. **Open WinSCP** → New Session
2. **Host name**: `YOUR_SERVER_IP`
3. **User name**: `master`
4. **Password**: Your Cloudways master password
5. Click **Login**
6. In the **left pane** (your PC): Navigate to where `keells-scraper` is
7. In the **right pane** (server): Navigate to `/tmp/`
8. **Drag** the entire `keells-scraper` folder from left to right

### Option C: Using VS Code Remote-SSH (if you have it)

1. Connect VS Code to your Cloudways server via Remote-SSH
2. Drag the `keells-scraper` folder into `/tmp/` on the server

### Also Upload credentials.json

```bash
# Make sure your Google OAuth credentials.json is also uploaded
scp credentials.json master@YOUR_SERVER_IP:/tmp/keells-scraper/
```

---

## Step 3: Move Files to Final Location

SSH into your server:

```bash
ssh master@YOUR_SERVER_IP
```

Now move the files to the application directory:

```bash
# CHOOSE ONE:
# Option A (simple name):
sudo mv /tmp/keells-scraper /home/master/applications/keells-scraper

# Option B (project-prefixed):
sudo mv /tmp/keells-scraper /home/master/applications/worldinflationtracker-keells
```

Fix ownership (Cloudways uses `master` user):

```bash
# Replace with your actual path:
sudo chown -R master:master /home/master/applications/keells-scraper
```

Verify files are in place:

```bash
ls -la /home/master/applications/keells-scraper/
# You should see: app.py, scraper.py, sheets.py, templates/, deploy.sh, etc.
```

---

## Step 4: Run the Deployment Script

```bash
cd /home/master/applications/keells-scraper
chmod +x deploy.sh
```

Now run the deploy script **with your chosen port**:

```bash
# If port 5001 is free:
APP_PORT=5001 ./deploy.sh

# If you need a different port, change it:
APP_PORT=5050 ./deploy.sh
```

**What this does:**
1. Installs system libraries (libxml2 for HTML parsing)
2. Creates a Python virtual environment (`venv/`)
3. Installs all Python packages from `requirements.txt`
4. Creates a Supervisor config to keep the app running 24/7
5. Sets up a weekly cron job (Monday 6 AM) as backup scheduler

If successful, you'll see: **"Deployment Complete!"** ✅

---

## Step 5: Verify Everything is Running

```bash
# Check supervisor process
sudo supervisorctl status keells-scraper
```

Expected output:
```
keells-scraper    RUNNING    pid 12345, uptime 0:00:15
```

If it says `FATAL` or `STOPPED`, check the error log:
```bash
cat /home/master/applications/keells-scraper/supervisor_err.log
```

---

## Step 6: Test the Web Dashboard

Open your browser:
```
http://YOUR_SERVER_IP:5001
```
(Replace `5001` with the port you chose)

You should see the **Login page** with a gradient background. ✅

**Can't reach it?** Cloudways has a firewall. You may need to open the port:

1. Go to your **Cloudways Platform Dashboard**
2. Navigate to **Servers → Your Server → Security → Firewall**
3. Add a new rule: Port `5001`, Protocol `TCP`, Source `0.0.0.0/0`
4. Click **Add Rule**

---

## Step 7: Google OAuth Authorization (One-Time)

Still on your SSH session:

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

https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=...
```

1. **Copy the full URL** and paste into your browser
2. Sign in with your Google account
3. Click **Advanced → Go to Keells Price Scraper (unsafe)** → **Continue**
4. Copy the authorization code
5. Paste it back in the SSH terminal and press Enter

You should see: `OAuth token saved to token.pickle` ✅

---

## Step 8: Share Your Google Sheet

1. Open your Google Sheet in a browser
2. Click **Share** (top right)
3. Enter **your own email address** (the one you authorized with)
4. Permission: **Editor**
5. Click **Send**

---

## Step 9: Configure via Web UI

1. Go to `http://YOUR_SERVER_IP:5001`
2. Login: `admin` / `keells2024!`
3. Click **Settings** in the top nav
4. Enter your **Google Spreadsheet ID** (from the sheet URL, between `/d/` and `/edit`)
5. Set your preferred **schedule** (day + time)
6. Click **💾 Save Settings**

---

## Step 10: Test the Scrape

1. Go to the **Dashboard**
2. Click **"▶ Run Scrape Now"**
3. Wait 1-3 minutes (it scrapes all 9 categories)
4. The page will refresh showing the result
5. Check your Google Sheet — you should see product prices! 🎉

---

## Optional: Nginx Reverse Proxy (recommended for HTTPS)

If you want to access the dashboard via a domain (e.g., `scraper.yourdomain.com`) with HTTPS, set up Nginx as a reverse proxy:

```bash
sudo nano /etc/nginx/sites-available/keells-scraper
```

Paste:
```nginx
server {
    listen 80;
    server_name scraper.yourdomain.com;   # CHANGE THIS

    location / {
        proxy_pass http://127.0.0.1:5001;  # CHANGE PORT if different
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Then:
```bash
sudo ln -s /etc/nginx/sites-available/keells-scraper /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

For HTTPS, use Let's Encrypt (if Cloudways allows it) or Cloudways' built-in SSL.

---

## Quick Commands for Ongoing Management

```bash
# Check if the app is running
sudo supervisorctl status keells-scraper

# Restart the app
sudo supervisorctl restart keells-scraper

# Stop the app
sudo supervisorctl stop keells-scraper

# View live logs
tail -f /home/master/applications/keells-scraper/scraper.log

# View web access logs
tail -f /home/master/applications/keells-scraper/access.log

# Run a manual scrape from command line
cd /home/master/applications/keells-scraper
source venv/bin/activate
python3 -c "
from app import load_config, execute_scrape
config = load_config()
execute_scrape(config)
"

# Check cron jobs
crontab -l | grep keells-scraper

# Update the app after modifying code
cd /home/master/applications/keells-scraper
source venv/bin/activate
pip install -r requirements.txt
sudo supervisorctl restart keells-scraper
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port already in use** | Run `sudo netstat -tlnp \| grep LISTEN` to see used ports; pick another |
| **Can't access web UI** | Check Cloudways firewall; open the port in Cloudways Dashboard |
| **Supervisor shows FATAL** | Run `cat supervisor_err.log` in the app directory |
| **credentials.json not found** | Upload it to the app directory: `scp credentials.json master@IP:/home/master/applications/keells-scraper/` |
| **OAuth code expired** | Re-run the authorization command from Step 7 |
| **Google Sheet not updating** | Share the sheet with your email (Editor access) |
| **0 products scraped** | Check if keellssuper.com is accessible from the server: `curl -I https://keellssuper.com` |

---

## Your Server Map (fill this out)

```
Server IP: ___________

Existing Applications:
  /home/master/applications/___________  → Port ___
  /home/master/applications/___________  → Port ___
  /home/master/applications/___________  → Port ___

Keells Scraper:
  /home/master/applications/___________  → Port ___
  Web URL: http://___________:__________
  Supervisor: keells-scraper