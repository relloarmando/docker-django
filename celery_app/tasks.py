from celery import shared_task
import json

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def print_task(message):
    print(f'This is a Celery Task: {message}')
