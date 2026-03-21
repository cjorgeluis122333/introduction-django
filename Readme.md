# Django

## Create and install all than you need for your project

Go to the route of your project and install this command in your cmd

```bash
   pip install virtualenv 

```

### Check if your environment version

```bash
 virtualenv --version 
```

### Create a folder for save your virtual env

```bash
# Para usar la versión más reciente instalada:(Recomendada)
py -m venv venv

# # Para usar la vesion por defecto
virtualenv venv
```

#### Activate the enviroment

```bash
 .\venv\Scripts\activate    
```

### Step 2: Install Django

```bash
pip install Django
```

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
  python manage.py makemigrations app_name_optional
```

* ***Level Project migration***: This migrations transform all you app migration in tables
  
```shell
  python manage.py migrate
```

### Sample with Migration

#### Step 1: Create the model in your app

Like Django use a ORM you first have to create a a class use the models imported like this: 

```py
from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    shop_id = models.ForeignKey(to=Shop, on_delete=models.CASCADE)

```

This model give the shape of the Table but is just that. Y you want fill the shape you need execute the next command

#### Step 2: Execute the command ***makemigrations***

This command take yours created model and create into the folder ***migrations*** a file  with a name like this: ***0001_initial.py***

```shell
  python manage.py makemigrations
```

The file create this command contains all your model class what not included in your last migration.
This file is very important so it's who make the orm allow cat to some DataBase

```py
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.shop')),
            ],
        ),
    ]

```

#### Step 3: Execute the command ***migration***

This is the last step because here you transform your migration in one database

```shell
  python manage.py migrate
```

## Profundizando en Rutas y Url

### URL with params like the @PathVariable() of java

* URL with path variable

Samples:

   ```text
    /api/product/1
    /api/product/1234
    /api/product/123/my_cat
   ```

In python you represent this url with this structure.

```py
  path("base_url/<int:param_name>", views.view_name)

  path("base_url/<str:param_name>", views.view_name)
```

Like you see the datatype can change

## Response

In views of your app you can defined two type of response

### HttpResponse

This response return  ***view***

```py

```

### JsonResponse

This response return a ***JSON***

```py

```


## Use the 