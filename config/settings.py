"""Django settings for the PYTHON_2.6 golden-repo fixture project.

Targets Django 1.5, the last release still supporting Python 2.6, so
this uses that era's settings API: MIDDLEWARE_CLASSES (renamed to
MIDDLEWARE in Django 1.10) and TEMPLATE_DIRS (superseded by the
TEMPLATES dict in Django 1.8).
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Intentionally hardcoded - a real SAST-style finding, not a synthetic
# fixture.
SECRET_KEY = 'fixture-only-not-for-production-2a6c9f1e73b0d4a8'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'catalog',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATE_DIRS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
