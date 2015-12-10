"""
Django settings for horse project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+(k#-e2yrqo%^f!ga0ka7f!yy_cv0)_uj-h$avn-tgah%9umzg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'chart_tools',
    'base',
    'flatlease',
    'car_leasing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'horse.urls'
LOGIN_URL = 'login'

ADMINS = (
    ('Vasiliy', 'menstenebris@gmail.com'),
)

MANAGERS = (
    ('Vasiliy', 'menstenebris@gmail.com'),
    ('Vera', 'securicula@gmail.com'),
)

SERVER_EMAIL = 'horse@django' # Адрес отправителя почты

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'horse.wsgi.application'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         # 'file': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.handlers.TimedRotatingFileHandler',
#         #     'when': 'd',
#         #     # 'interval': '1',
#         #     'encoding': 'UTF8',
#         #     'formatter': 'simple',
#         #     'filename': '/var/log/horse/debug.log',
#         # },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'encoding': 'UTF8',
#             'formatter': 'verbose',
#             'filename': '/var/log/horse/debug.log',
#         },
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'console', 'file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'flatlease': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.security.DisallowedHost': {
#             'handlers': ['mail_admins'],
#             'propagate': False,
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '52.28.14.84',
        'PORT': '5432',
        'NAME': 'horse',
        'USER': 'django',
        'PASSWORD': '14875264',
    },
    'flat': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '52.28.14.84',
        'PORT': '5432',
        'NAME': 'flat',
        'USER': 'django',
        'PASSWORD': '14875264',
    },
    'car': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '52.28.14.84',
        'PORT': '5432',
        'NAME': 'car',
        'USER': 'django',
        'PASSWORD': '14875264',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru'



TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = (
    '%d.%m.%Y', '%d.%m.%Y', '%d.%m.%y',  # '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',  # '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',  # '25 Oct 2006',
    '%d %B %Y',  # '25 October 2006',
    '%d.%m.%Y',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'