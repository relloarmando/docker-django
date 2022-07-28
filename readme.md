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

You'll need 2 terminal to start Celery Tasks

Worker:
``` console
celery -A composeexample worker --pool=solo --loglevel=info
 ```
![image](https://user-images.githubusercontent.com/92693998/181430485-f731358b-83ab-4d8f-a93f-5b0c600b40f9.png)

Beat:
``` console
celery -A composeexample beat -l info
```
![image](https://user-images.githubusercontent.com/92693998/181430439-768ad81c-aa22-456b-a59e-8fb73b819381.png)

Login to Django Admin with your superuser credentials

![image](https://user-images.githubusercontent.com/92693998/181433172-ab6c0498-3043-469c-97ce-d4fdeecccabf.png)

From this panel you can view, edit and create Celery tasks
 
## Sources 
 1. https://django-celery-beat.readthedocs.io/en/latest/
 2. https://www.youtube.com/watch?v=fBfzE0yk97k
 3. https://stackoverflow.com/questions/67001563/no-errors-but-celery-task-not-sending-email-as-expected
 
