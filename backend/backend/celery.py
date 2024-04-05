from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config
from django.conf import settings


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend',
             broker_url=settings.CELERY_BROKER_URL,
             backend=settings.CELERY_RESULT_BACKEND )

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

print(f"CELERY_APP: {app}")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
