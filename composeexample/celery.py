import os

from celery import Celery
# from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'composeexample.settings')

app = Celery('composeexample')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'celery.py_message': {
        'task': 'composeexample.tasks.celery_message',
        'schedule': 10.0,
        'args': (['Programmed from celery.py'])
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
