# Instructions
``` console
git clone https://github.com/relloarmando/docker-django.git
 ```

## For Windows 10 or 11:
Install prerequisites ([ref. 1](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#prerequisites)) : 
* Wsl Version 2
* Install Linux distro 
* Windows Terminal
_This was tested on Windows 11 and wsl-2 Ubuntu_

To be sure, check your current version of wsl 
``` console
 wsl -l -v
 ```
 
* Download and install docker desktop for windows ([ref. 2](https://docs.docker.com/desktop/windows/wsl/)), then open Docker-Desktop
![image](https://user-images.githubusercontent.com/92693998/181148879-87dbb44d-7374-4ec4-99b7-7caa2e14825c.png)


In a windows terminal cd to directory
``` console
 cd docker-django
 ```

Create the Django project ([ref. 3](https://docs.docker.com/samples/django/)) by running the command as follows: 
``` console
docker-compose run web django-admin startproject composeexample .
 ```
 ![image](https://user-images.githubusercontent.com/92693998/180701921-40be16f1-80ef-414f-87f5-ade33ec73d54.png)

 
After the image has finished building, start the project:
``` console
docker-compose up
 ```
 ![image](https://user-images.githubusercontent.com/92693998/180700775-a99e6475-8cf5-4d69-8a59-4dad06549e72.png)
 ### When the services docker-django-db and docker-django-web are up,
 visit http://127.0.0.1:8000/first-app/my-first-page
 ![image](https://user-images.githubusercontent.com/92693998/180701300-7f02472c-2916-4456-b832-28952f71d529.png)

### Congratulations !! You have deployed a django server and a postgres database
 
 
## Sources 
 1. https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#prerequisites
 2. https://docs.docker.com/desktop/windows/wsl/
 3. https://docs.docker.com/samples/django/
 4. https://www.w3schools.com/django/django_templates.php
