from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.decorators import task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_view_test.settings')

app = Celery('model_view_test')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def add(x, y):
    return x + y