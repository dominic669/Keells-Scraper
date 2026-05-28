"""Gunicorn Configuration for Cloudways (2GB Memory)

Optimized for a single-worker, memory-efficient deployment.
The app is lightweight and only runs once/week, so 1 worker is sufficient.
"""

bind = "0.0.0.0:5000"
workers = 1          # Single worker for 2GB memory
threads = 2          # 2 threads for handling web UI requests
preload_app = True   # Share resources across threads
timeout = 600        # 10 min timeout for long scrape runs
max_requests = 100   # Recycle worker after 100 requests (memory hygiene)
max_requests_jitter = 10
loglevel = "info"
accesslog = "access.log"
errorlog = "error.log"

# Memory efficiency settings
worker_class = "gthread"  # Threaded worker
worker_connections = 10
keepalive = 5