"""
Django settings for h2100 project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1!3)52_eu&!5k*2j7z3e@ay2i9v=l0_qud2c29&@&zoeh!yqsv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hackingto100.com', 'www.hackingto100.com', 'h2100.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'django_forms_bootstrap',
    'django_hosts',

    # Local Apps
    'analytics',
    'blog',
    'shortener',
)

MIDDLEWARE_CLASSES = (
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
)

ROOT_URLCONF = 'h2100.urls'
ROOT_HOSTCONF = 'h2100.hosts'
DEFAULT_HOST = 'www'
DEFAULT_REDIRECT_URL = "http://www.hackingto100.com"
PARENT_HOST = "hackingto100.com"

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

WSGI_APPLICATION = 'h2100.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'h2100.db'),
    }
}

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password Validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
# {
#     'NAME': 'django.contrib.auth.password_validation.UserAttributesSimilarityValidator',
# },
# {
#     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# },
# {
#     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# },
# {
#     'NAME': 'djanto.contrib.auth.password_validation.NumericPasswordValidator',
# },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Anchorage'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# If SHORTCODE variables are changed, migrate dbase because these change the models
SHORTCODE_MAX = 16
SHORTCODE_MIN = 4


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# STATIC_ROOT is where files are collected to be served when going live
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_in_venv', 'static_root')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
# STATIC_ROOT = "/var/www/example.com/static/"
# Path also could be: os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'static_root')

# We put our files in STATICFILES_DIRS; could include ,'/var/www/static',
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#    os.path.join(BASE_DIR, 'static', 'h2_static'),
#     )

# Media is where user-uploaded files go
# MEDIA_URL= '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



