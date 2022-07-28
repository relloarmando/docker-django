# Instructions for Celery Periodic Tasks
``` console
git clone https://github.com/relloarmando/docker-django.git
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
 ![image](https://user-images.githubusercontent.com/92693998/181424915-f801dc59-5b1e-42e2-94db-c9a251f293d7.png)

``` console
python manage.py migrate
 ```
 ![makemigrations](https://user-images.githubusercontent.com/92693998/181426114-3a527cc2-b205-44d3-b44d-5d6e5c9c1fc3.png)

Create a superuser to login in django admin
``` console
python manage.py createsuperuser
 ```

 Login http://127.0.0.1:8000/admin
 ![django_admin_celery](https://user-images.githubusercontent.com/92693998/181426174-a911b845-04c9-4d0c-99f6-84cbaf522551.png)



 
 
## Sources 
 1. https://django-celery-beat.readthedocs.io/en/latest/
 2. https://www.youtube.com/watch?v=fBfzE0yk97k
 3. https://stackoverflow.com/questions/67001563/no-errors-but-celery-task-not-sending-email-as-expected
 
