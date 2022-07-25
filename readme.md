# Instructions
### git clone https://github.com/relloarmando/docker-django.git

## For Windows 10 or 11:
### install wsl VERSION 2, then proceed to install Linux distro (1) "This was tested on Windows 11 and wsl-2 Ubuntu"

### Command to check your current version of wsl 
``` console
 wsl -l -v
 ```

### Once you have wsl-2 and a linux distro, download and install docker desktop for windows (2)

### cd to directory
``` console
 cd docker-django
 ```

### Create the Django project by running the docker compose run command as follows (3)
``` console
docker-compose run web django-admin startproject composeexample .
 ```
 
 ### After the image finished building, start the project
``` console
docker-compose up
 ```
 ![image](https://user-images.githubusercontent.com/92693998/180700775-a99e6475-8cf5-4d69-8a59-4dad06549e72.png)
 ### When the services dicker-django-db and docker-django-web are up, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/first-app/my-first-page)
 
 
## Sources 
### *1 https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers 
### *2 https://docs.docker.com/desktop/windows/wsl/
### *3 https://docs.docker.com/samples/django/
### *4 https://www.w3schools.com/django/django_templates.php
