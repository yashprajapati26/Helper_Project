"""
Django settings for helper_project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3tib2szg05m6x#!731fwbz%xh%9i*_3f3##bmdwv(4)2jy#0^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'location_field.apps.DefaultConfig',
    'helper_app',
    'vendor_app',
    'dyanamic_app',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    # for api app and 3rd party app 
    'api_app',
    'rest_framework',
    'knox',
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helper_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'helper_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'test_db_2',
       'USER': 'postgres',
       'PASSWORD': 'agc123',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'NAME': 'test_db_3',
#        'USER': 'postgres',
#        'PASSWORD': 'agc123',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
# }
# test_db


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "helper_app.User"


# EMAIL_HOST_USER= 'my422kingheart.2728@gmail.com'
# EMAIL_HOST_PASSWORD= 'wuyghwxrgvwnnixs'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'projectPY2@gmail.com'
EMAIL_HOST_PASSWORD = 'qhkbtgmlavcsqfpp'



# LOCATION_FIELD = {
#     'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
#     'provider.google.api_key': 'promising-lamp-357010',
#     'provider.google.api_libraries': '',
#     'provider.google.map.type': 'ROADMAP',
# }
LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'search.provider': 'nominatim',
}
# LOCATION_FIELD_PATH = settings.STATIC_URL + 'location_field'
#
# LOCATION_FIELD = {
#     'map.provider': 'google',
#     'map.zoom': 13,
#
#     'search.provider': 'google',
#     'search.suffix': '',
#
#     # Google
#     'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
#     'provider.google.api_key': 'promising-lamp-357010',
#     'provider.google.api_libraries': '',
#     'provider.google.map.type': 'ROADMAP',
#
#     # Mapbox
#     'provider.mapbox.access_token': 'https://oauth2.googleapis.com/token',
#     'provider.mapbox.max_zoom': 18,
#     'provider.mapbox.id': 'mapbox.streets',
#
#     # OpenStreetMap
#     'provider.openstreetmap.max_zoom': 18,
#
#     # misc
#     'resources.root_path': LOCATION_FIELD_PATH,
#     'resources.media': {
#         'js': (
#             LOCATION_FIELD_PATH + '/js/form.js',
#         ),
#     },
# }
# GEOS_LIBRARY_PATH = ''


##############################################
######  for Django rest api permissions ######
##############################################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}


APPEND_SLASH=False