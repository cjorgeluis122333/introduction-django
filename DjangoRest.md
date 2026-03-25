# Django Rest Framework

Is a super framework of django and provide him with rest functionalities

## Get started

If you want a project with this characteristics you should install:

1. Install the virtual env
2. Install django
3. Install django rest framework

### Step 1: Install the virtual env

```bash
   pip install virtualenv 
```

```bash
python -m virtualenv venv
```

```bash
 .\venv\Scripts\activate    
```

### Step 2: Install the Django

```bash
pip install django
```

### Step 3: Install the Django Rest Framework

```shell
pip install djangorestframework
```

### Step 4: Create a project Django

```bash
django-admin startproject project_name . 
```

### Step 5: Create app

```bash
python manage.py startapp app_name
```

### Step 6: Config setting for use django

1. Go to your project django -> setting.py
2. Search de var INSTALLED_APPS and append in the end:

```py
    #This is the module of django rest [Obligatory for add django]
    'rest_framework',
    # The app do you create
    'mi_app',
```

### Step 7: Run the server

```bash
python manage.py runserver 8000
```

## Serializers

The serializers is a new concept include ***django test***. They work up the models givings rules to this models.

1. Create the model
2. Migrate this model
3. Create a file ***serializers.py***
4. Configure this file

### Sample

#### Create the model

```py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    create_at = models.DateField(auto_now_add=True)
    
```

#### Create the serialized

Into your create file ***serializers.py*** implement this logic:

```py
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','description','technology','create_at')
        read_only_fields = ('create_at')
```

* model: Reference the model
* fields: The field will show in the request
* read_only_fields: The fields do not received update

## URLS and Api

1. Create a file api.py
2. Define your viewset
3. Create a file urls.py
4. Append this url created in your django app to your urls of your django project

```py
from rest_app_project.serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectSerializer
```

This class is a middleware where you define the kind of petition can see this Serializer.

### URL

You have to create this file like django but this time you will use a new functionality of this framework: ***routers***

```py
from rest_framework import routers
from rest_app_project.api import ProjectViewSet
from .api import ProjectViewSet

routers = routers.DefaultRouter()
routers.register(
    prefix='api/projects',
    viewset=ProjectViewSet,
    basename='projects'
    
```

This generate the rout of all methods (GET, POST, PUT, DELETE) in just one line

* prefix: The path of your project
* viewset: Your api viewset class
* basename

## All your dependencies

```py
pip freeze > requirements.txt
```

