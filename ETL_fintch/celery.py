from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ETL_fintch.settings')

app = Celery('ETL_fintch')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: [app_config.name for app_config in apps.get_app_configs()])

app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    beat_schedule={
        'update_stock_data': {
            'task': 'data_extraction.scripts.tasks.update_stock_data',
            'schedule': 60.0,
        },
    },
)
