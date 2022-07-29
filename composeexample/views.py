from celery import shared_task
from django.http import HttpResponse


def home(request):
    return HttpResponse(" <h1> Home Page </h1> ")


@shared_task
def celery_message(message):
    print(f'Celery Task {message}')
