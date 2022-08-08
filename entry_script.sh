#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
celery -A composeexample worker --pool=solo --loglevel=info &
celery -A composeexample beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
tail -f /dev/null