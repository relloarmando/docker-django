from celery import shared_task


@shared_task
def celery_message(message):
    print(message)
    print(f'Celery Task {message}')
