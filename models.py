"""Data models for the Keells scraper app"""
import json
import os
import uuid
import hashlib
from datetime import datetime, timedelta
from flask_login import UserMixin

DATA_DIR = 'data'


class User(UserMixin):
    """Simple admin user for web interface login"""

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
    """Represents a single scrape execution"""

    def __init__(self, run_id, week_label, status, started_at, finished_at,
                 total_products, category_stats, sheet_updated, error):
        self.id = run_id
        self.week_label = week_label
        self.status = status  # 'running', 'success', 'failed'
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
            return str(delta).split('.')[0]
        return 'N/A'

    @property
    def success_rate(self):
        if not self.category_stats:
            return 'N/A'
        total = len(self.category_stats)
        success = sum(1 for v in self.category_stats.values() if v.get('status') == 'success')
        return f"{success}/{total}" if total > 0 else '0/0'

    def to_dict(self):
        return {
            'id': self.id,
            'week_label': self.week_label,
            'status': self.status,
            'started_at': self.started_at,
            'finished_at': self.finished_at,
            'duration': self.duration,
            'total_products': self.total_products,
            'category_stats': self.category_stats,
            'sheet_updated': self.sheet_updated,
            'success_rate': self.success_rate,
            'error': self.error
        }

    @classmethod
    def create(cls):
        """Create a new run record"""
        os.makedirs(DATA_DIR, exist_ok=True)
        run_id = datetime.now().strftime('%Y%m%d-%H%M%S-') + uuid.uuid4().hex[:6]
        week_label = cls._get_week_label()

        run = cls(
            run_id=run_id,
            week_label=week_label,
            status='running',
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
        """Mark run as completed"""
        self.status = 'success' if success else 'failed'
        self.finished_at = datetime.now().isoformat()
        self.error = error
        self._save()

    def _save(self):
        """Persist run to disk as JSON"""
        os.makedirs(DATA_DIR, exist_ok=True)
        filepath = os.path.join(DATA_DIR, f'{self.id}.json')
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2, default=str)

    @classmethod
    def get(cls, run_id):
        """Load a specific run from disk"""
        filepath = os.path.join(DATA_DIR, f'{run_id}.json')
        if not os.path.exists(filepath):
            return None
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(**data)

    @classmethod
    def get_recent(cls, limit=10):
        """Get most recent runs, newest first"""
        os.makedirs(DATA_DIR, exist_ok=True)
        files = sorted(
            [f for f in os.listdir(DATA_DIR) if f.endswith('.json')],
            reverse=True
        )[:limit]

        runs = []
        for fname in files:
            with open(os.path.join(DATA_DIR, fname), 'r') as f:
                data = json.load(f)
        runs.append(cls(
    run_id=data.get('id'),
    week_label=data.get('week_label'),
    status=data.get('status'),
    started_at=data.get('started_at'),
    finished_at=data.get('finished_at'),
    total_products=data.get('total_products'),
    category_stats=data.get('category_stats'),
    sheet_updated=data.get('sheet_updated'),
    error=data.get('error')
))
        return runs

    @staticmethod
    def _get_week_label():
        """Generate a week label like '2026-W22 (May 25 - May 31)'"""
        now = datetime.now()
        iso = now.isocalendar()
        week_num = iso[1]
        year = iso[0]
        # Monday of this week
        monday = now - timedelta(days=now.weekday())
        sunday = monday + timedelta(days=6)
        return f"{year}-W{week_num:02d} ({monday.strftime('%b %d')} - {sunday.strftime('%b %d')})"