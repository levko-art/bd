import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bd_service.settings')

app = Celery('bd_service')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
