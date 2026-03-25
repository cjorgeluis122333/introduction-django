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
