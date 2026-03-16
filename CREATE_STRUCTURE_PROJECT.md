# 📋 Guía Completa: Creación y Escalado de Proyectos Django

**Última actualización**: Marzo 2026  
**Versión Django**: 6.0.3  
**Python**: 3.14+

---

## 📑 Tabla de Contenidos

1. [Creación desde cero](#creación-desde-cero)
2. [Configuración inicial](#configuración-inicial)
3. [Estructura de carpetas recomendada](#estructura-de-carpetas-recomendada)
4. [Comandos esenciales](#comandos-esenciales)
5. [Escalando el proyecto](#escalando-el-proyecto)
6. [Mejores prácticas](#mejores-prácticas)
7. [Solución de problemas](#solución-de-problemas)

---

## 🚀 Creación desde cero

### Paso 1: Crear el directorio del proyecto

```bash
mkdir mi_proyecto_django
cd mi_proyecto_django
```

### Paso 2: Crear el entorno virtual

```bash
# Windows (CMD o PowerShell)
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**Verificar activación**: El nombre del entorno (`venv`) debe aparecer al inicio de la línea.

### Paso 3: Instalar Django

```bash
pip install django
```

**Verificar instalación**:

```bash
python -m django --version
# Debería mostrar: 6.0.3
```

### Paso 4: Crear el proyecto Django

```bash
django-admin startproject mi_proyecto .
```

**Nota**: El `.` al final crea el proyecto en la carpeta actual. Esto genera:

```file
mi_proyecto/
├── __init__.py
├── asgi.py
├── settings.py  ← Configuración principal
├── urls.py      ← Rutas globales
└── wsgi.py

manage.py        ← Script para comandos
```

### Paso 5: Crear la primera app

```bash
python manage.py startapp mi_app
```

Genera:
```
mi_app/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py      ← CREAR MANUALMENTE (no se genera automáticamente)
└── views.py
```

---

## ⚙️ Configuración inicial

### Paso 6: Registrar la app en `settings.py`

Edita `mi_proyecto/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'mi_app',  # ← Añade tu app aquí
]
```

### Paso 7: Configurar templates y archivos estáticos

En `settings.py`, busca y actualiza:

```python
# Añade al inicio del archivo
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Templates globales
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← Carpeta global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # ← Carpeta global de estáticos
```

### Paso 8: Configurar SECRET_KEY y DEBUG para ambientes

En `settings.py`, usa variables de entorno:

```python
import os

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-default-key-for-development'  # Solo en desarrollo
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
```

### Paso 9: Actualizar las rutas principales

En `mi_proyecto/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),  # ← Incluye rutas de mi_app
]
```

### Paso 10: Crear rutas para la app

Crea `mi_app/urls.py`:

```python
from django.urls import path
from . import views

app_name = "mi_app"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
```

---

## 📁 Estructura de carpetas recomendada

```
mi_proyecto_django/
│
├── venv/                          # Entorno virtual (no commitar)
│
├── mi_proyecto/                   # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── mi_app/                        # Primera app
│   ├── migrations/
│   ├── templates/mi_app/          # Templates específicos de esta app
│   │   └── home.html
│   ├── static/mi_app/             # Estáticos específicos
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/                     # Templates globales
│   └── base.html                  # Template base
│
├── static/                        # Archivos estáticos globales
│   ├── css/styles.css
│   └── img/favicon.ico
│
├── manage.py
├── requirements.txt               # Dependencias
├── .env                           # Variables de entorno (no commitar)
├── .gitignore
├── db.sqlite3                     # Base de datos (no commitar)
└── CREATE_STRUCTURE_PROJECT.md    # Este archivo
```

---

## 🛠️ Comandos esenciales

### Iniciar el servidor de desarrollo

```bash
# Activar el entorno virtual (si no está activo)
.\venv\Scripts\activate

# Ejecutar servidor
python manage.py runserver

# En navegador: http://127.0.0.1:8000/
```

### Migraciones (base de datos)

```bash
# Crear migraciones (después de cambiar models.py)
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones
python manage.py showmigrations
```

### Crear superusuario (admin)

```bash
python manage.py createsuperuser

# Te pedirá:
# - Username: (nombre de usuario)
# - Email: (correo)
# - Password: (contraseña)

# Acceder a: http://127.0.0.1:8000/admin/
```

### Validar configuración

```bash
python manage.py check
```

### Recopilar archivos estáticos (para producción)

```bash
python manage.py collectstatic --noinput
```

### Crear nueva app

```bash
python manage.py startapp nombre_app

# Luego:
# 1. Registrar en INSTALLED_APPS (settings.py)
# 2. Crear nombre_app/urls.py
# 3. Incluir en urls.py principal
```

### Shell interactivo de Django

```bash
python manage.py shell

# Ejemplo dentro del shell:
# >>> from mi_app.models import MiModelo
# >>> MiModelo.objects.all()
```

### Generar requirements.txt

```bash
pip freeze > requirements.txt
```

### Instalar desde requirements.txt

```bash
pip install -r requirements.txt
```

---

## 📈 Escalando el proyecto

### Fase 1: Proyecto pequeño (1-2 apps)

**Estructura actual**: Está bien como está.

**Qué cambiar**: Nada por ahora.

---

### Fase 2: Proyecto en crecimiento (3-5 apps)

Crea nuevas apps por funcionalidad:

```bash
python manage.py startapp usuarios
python manage.py startapp blog
python manage.py startapp api
```

Actualiza `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'mi_app',
    'usuarios',
    'blog',
    'api',
]
```

Actualiza `mi_proyecto/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
]
```

---

### Fase 3: Proyecto grande (5+ apps, equipos)

#### 3.1. Separar configuración por ambiente

Crea `mi_proyecto/settings/`:

```
mi_proyecto/settings/
├── __init__.py
├── base.py       # Config común
├── dev.py        # Config desarrollo
└── prod.py       # Config producción
```

`base.py`:
```python
# Configuración común a todos los ambientes
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INSTALLED_APPS = [...]
MIDDLEWARE = [...]
# ... resto de config común
```

`dev.py`:
```python
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

`prod.py`:
```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['tudominio.com']
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

Ejecutar con:
```bash
# Desarrollo
python manage.py runserver --settings=mi_proyecto.settings.dev

# Producción
python manage.py migrate --settings=mi_proyecto.settings.prod
```

#### 3.2. Organizar apps en carpetas lógicas

```
apps/
├── usuarios/
├── blog/
├── compras/
└── api/
```

Actualizar `INSTALLED_APPS` en `settings/base.py`:
```python
INSTALLED_APPS = [
    ...,
    'apps.usuarios',
    'apps.blog',
    'apps.compras',
    'apps.api',
]
```

#### 3.3. Cambiar de SQLite a PostgreSQL (producción)

Instalar driver:
```bash
pip install psycopg2-binary
```

En `settings/prod.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### 3.4. Agregar autenticación y permisos avanzados

```python
# En models.py de una app
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

# En settings.py
AUTH_USER_MODEL = 'usuarios.CustomUser'
```

#### 3.5. Usar Django REST Framework para API

```bash
pip install djangorestframework
```

En `settings.py`:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

---

## ✅ Mejores prácticas

### 1. Siempre usar entorno virtual

```bash
# Verificar activación
which python  # macOS/Linux
where python  # Windows

# Debe apuntar a: .../venv/bin/python
```

### 2. Mantener `.env` fuera de Git

Crea `.gitignore`:
```
venv/
.env
*.pyc
__pycache__/
db.sqlite3
*.log
.DS_Store
```

### 3. Usar variables de entorno

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
```

Instalar:
```bash
pip install python-dotenv
```

### 4. Usar migraciones correctamente

```bash
# SIEMPRE después de cambiar models.py
python manage.py makemigrations

# ANTES de cualquier deploy
python manage.py migrate
```

### 5. Logging en producción

En `settings/prod.py`:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

### 6. Cache para rendimiento

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

Instalar Redis:
```bash
pip install redis
```

### 7. Tests automáticos

En `mi_app/tests.py`:
```python
from django.test import TestCase, Client

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mi_app/home.html')
```

Ejecutar tests:
```bash
python manage.py test

# Con cobertura
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML
```

---

## 🐛 Solución de problemas

### Error: "ModuleNotFoundError: No module named 'django'"

**Causa**: Entorno virtual no activado.

**Solución**:
```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### Error: "TemplateSyntaxError: Invalid block tag on line X: 'static'"

**Causa**: No cargas `{% load static %}` en el template.

**Solución**: Añade al inicio del template:
```django
{% load static %}
```

---

### Error: "django.template.exceptions.TemplateDoesNotExist"

**Causa**: Template no encontrado.

**Solución**: Verifica:
1. Que la ruta en `template_name` sea correcta.
2. Que `APP_DIRS = True` en `settings.py`.
3. Que la carpeta `templates/` esté configurada en `DIRS`.

---

### Error: "No such table: auth_user"

**Causa**: Migraciones no aplicadas.

**Solución**:
```bash
python manage.py migrate
```

---

### Error: "Port 8000 already in use"

**Causa**: El servidor ya está ejecutándose.

**Solución**:
```bash
# Usar otro puerto
python manage.py runserver 8001

# O matar el proceso (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

### Performance lento en desarrollo

**Soluciones**:
```bash
# Desactivar reloader
python manage.py runserver --noreload

# Usar otro servidor ASGI (más rápido)
pip install daphne
python manage.py runserver --asgi
```

---

## 📚 Recursos útiles

- [Documentación oficial Django](https://docs.djangoproject.com/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)

---

## 🎯 Checklist rápido para nuevos proyectos

- [ ] Crear carpeta y cd
- [ ] `python -m venv venv`
- [ ] Activar venv
- [ ] `pip install django`
- [ ] `django-admin startproject proyecto .`
- [ ] `python manage.py startapp app1`
- [ ] Registrar app en `INSTALLED_APPS`
- [ ] Crear `app1/urls.py`
- [ ] Incluir en `urls.py` principal
- [ ] Crear `templates/` y `static/`
- [ ] `python manage.py migrate`
- [ ] `python manage.py createsuperuser`
- [ ] `python manage.py runserver`
- [ ] `pip freeze > requirements.txt`
- [ ] Crear `.gitignore`

---

**¡Listo!** Ahora tienes una guía completa para crear y escalar proyectos Django. 🚀
