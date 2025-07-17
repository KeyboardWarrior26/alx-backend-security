from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Schedule periodic tasks here or use celery beat schedule in settings.py
app.conf.beat_schedule = {
    'detect-suspicious-ips-every-hour': {
        'task': 'ip_tracking.tasks.detect_suspicious_ips',
        'schedule': 3600.0,  # every hour
    },
}

