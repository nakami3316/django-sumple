"""
Django settings for sample project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os #追加

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #デプロイ

#変更

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',##ココ追加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ##デプロイ
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    ##
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates')##ココ追加
        ],
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
#######################################################
WSGI_APPLICATION = 'sample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#追加

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

from socket import gethostname
hostname = gethostname()

if "LAPTOP-O21QPAN7" in hostname:
    # デバッグ環境
    # DEBUG = True 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ALLOWED_HOSTS = ['*'] 
else:
    # 本番環境
    # DEBUG = False
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES = {
        'default': dj_database_url.config()
    }
    ALLOWED_HOSTS = ['*']


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')#デプロイ
STATIC_URL = 'static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, "static"),##ココ追加
STATIC_ROOT = os.path.join(BASE_DIR, 'static')#デプロイ


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Heroku database
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# db_from_env = dj_database_url.config(conn_max_age=600,
# ssl_require=True)
# DATABASES['default'].update(db_from_env)
# try:
#  from .local_settings import *
# except ImportError:
#  pass
if not DEBUG:
  SECRET_KEY = '***************************************' #削除したSECRET_KEYをコピペします

import django_heroku
django_heroku.settings(locals())