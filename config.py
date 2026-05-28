"""Application Configuration"""
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-to-a-random-secret-key-in-production')
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

    # Scraper settings
    REQUEST_TIMEOUT = 30  # seconds
    REQUEST_DELAY = 0.5   # seconds between requests (be polite)
    MAX_RETRIES = 3