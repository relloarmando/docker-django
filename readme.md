# Why use Celey tasks with Django
Sending an email, processing a file, or processing heavy computations will keep our execution and the user waiting for the task to complete. Celery, in combination with Django, solves the problem of the model request-response not being asynchronous and you can also gives you the functionality to create recurring tasks with celery and django. Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system. It’s a task queue with focus on real-time processing, while also supporting task scheduling.

![image](https://user-images.githubusercontent.com/92693998/181683394-ee40b718-0841-4ca5-9f56-c8db75c4552e.png)
_https://coffeebytes.dev/celery-y-django-para-ejecutar-tareas-asincronas/_


# Instructions for Celery Periodic Tasks
``` console
git clone https://github.com/relloarmando/docker-django.git --branch celery_tasks
 ```

In a windows terminal cd to directory
``` console
 cd docker-django
 ```
 
Start the containers with the following command:
``` console
docker-compose up
 ```
![docker-django-compose-up](https://user-images.githubusercontent.com/92693998/181424343-b1f43a2b-4121-46d2-aa3f-ba6badb0ecf6.png)

When the services are up, enter the container to run commands:
``` console
docker ps
 ```

``` console
docker exec -it [container-name-or-id] bash
 ```
 ![docker_exec](https://user-images.githubusercontent.com/92693998/181424915-f801dc59-5b1e-42e2-94db-c9a251f293d7.png)

``` console
python manage.py migrate
 ```
 
![migrations](https://user-images.githubusercontent.com/92693998/181427487-9463d5ab-893d-4a32-9d9e-465c3011ce22.png)


Create a superuser to login in django admin, then exit the terminal
``` console
python manage.py createsuperuser

exit
 ```

You'll need to start 2 terminals for the worker and beat in the container docker-django-web.
To get the CONTANER ID
``` console
docker ps
```
![image](https://user-images.githubusercontent.com/92693998/181682399-04b91fba-e724-4e0f-8419-05dd25ac4c4e.png)

Worker:
``` console
docker exec [CONTAINER ID] celery -A composeexample worker --pool=solo --loglevel=info
 ```
![image](https://user-images.githubusercontent.com/92693998/181682534-9dbe848b-8226-456a-9c27-64d26dc59166.png)


Beat:
``` console
docker exec -it [CONTAINER ID] celery -A composeexample beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
![image](https://user-images.githubusercontent.com/92693998/181682649-07e11d48-2258-4f52-9d5d-6e6a1b28cf87.png)

# How to schedule periodic tasks with Django and Celery 
Here is showed 2 ways of scheduling periodic task in django-celery
1. Write beat_schedule dictionary in composeexample/celery.py
![image](https://user-images.githubusercontent.com/92693998/181691288-00497b2b-2ce8-42a8-9ada-a0eed5c04c7a.png)

2. Login to Django Admin with your previously superuser credentials
From this panel you can view, edit and create Celery tasks
![image](https://user-images.githubusercontent.com/92693998/181691804-b16f867c-68d0-4f81-b5e1-f4c9d8d6b387.png)
![image](https://user-images.githubusercontent.com/92693998/181692028-0a2e64bf-03e6-4f2c-ba1c-34d1ad7da19f.png)


 
## Sources 
 1. https://django-celery-beat.readthedocs.io/en/latest/
 2. [Learn Django Celery with RabbitMQ - Install and create new celery instance](https://www.youtube.com/watch?v=fBfzE0yk97k)
 3. https://stackoverflow.com/questions/67001563/no-errors-but-celery-task-not-sending-email-as-expected
 
