# Django Concepts

## Create Django project

This project will be the entry point.
All your config born here.
You bind every app in the files created with this command. 

```bash
django-admin startproject project_name . 
```

## Create a App

Every app of django contain a compacted logic, you can imagine a app like a module.
In django your structure will be:

```txt
 shopping_project
    ----app_authentication
    ----app_security
    ----app_sell_product
    ----app_inventario
    ----app_employ
```

You have a project and inside his project you will has a lot of app every app make a
functionality of this project.

```bash
python manage.py startapp app_name
```

## Run the server

```bash
python manage.py runserver 8000
```

## Bind a app

1. Open your project folder
2. Open the file ***settings/py***
3. Go to the var: ***INSTALLED_APP***
4. In the end write the name of your app

### Sample

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'mi_app',
    'product_app'
]

```

## Url

The url is the endpoint of your app. Here you defined a reference to your method in your App_module.
Exist two way of defined urls:

1. Reference ono to one of every method of your every app.
2. Create a url file in every app and them reference this file in your project url.py

## Migration

Here inside two kind of migration:

* ***Level App migration***: This migration exist for transform a simple model of python y a table

```shell
   python manage.py makemigration app_name_optional
```

* ***Level Project migration***: This migrations transform all you app migration in tables
  
```shell
  python manage.py migration
```

