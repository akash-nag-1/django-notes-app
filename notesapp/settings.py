import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&dzi#zsb(hz6p(s#anunt&#-a%ohr2hld71*i72*^exvw-yq$y'

DEBUG = True

# For development, allow all hosts. For production, specify exact domains.
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # ... your apps ...
]

MIDDLEWARE = [
    # ... your middleware ...
]

ROOT_URLCONF = 'notesapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'mynotes/build'],  # your React or frontend build folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ... your context processors ...
            ],
        },
    },
]

WSGI_APPLICATION = 'notesapp.wsgi.application'

# Use environment variables for DB credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'default_db_name'),        # Provide default if needed
        'USER': os.getenv('DB_USER', 'default_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'default_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}

# Password validation (unchanged)
AUTH_PASSWORD_VALIDATORS = [
    # ... your validators ...
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings

STATIC_URL = '/static/'

# Your React or frontend build static files folder
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'mynotes/build/static')]

# Where collectstatic will collect static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
