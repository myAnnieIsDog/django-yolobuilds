"""
Django settings for yolobuilds project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+am2krzl640b-p6y^)d3h=b)-e@)52t$+w)lijb^1e3u&&6wc0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_extensions',
    'pandas',
    'numpy',
    'openpyxl',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_bootstrap5',
    'django_htmx',
    'django_recaptcha',

    'permits.apps.PermitsConfig',
    'permits_bp.apps.PermitsBPConfig',
    
    'fees.apps.FeesConfig',
    'general.apps.GeneralConfig',
    'inspections.apps.InspectionsConfig',
    'locations.apps.LocationsConfig',
    'payments.apps.PaymentsConfig',
    'profiles.apps.ProfilesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'yolobuilds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/', 
            'yolobuilds/templates/'],
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

WSGI_APPLICATION = 'yolobuilds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'default': {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "sdoolittle$yolobuilds",
    #     "USER": "sdoolittle",
    #     "PASSWORD": "e9ci2J8MAutNYY#",
    #     "HOST": "sdoolittle.mysql.pythonanywhere-services.com", # "ssh.pythonanywhere.com"
    # },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

LOGIN_URL = ["profile/login/"]
LOGIN_REDIRECT_URL = [""]
LOGOUT_REDIRECT_URL = [""]

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "yolobuilds/static"
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = 'bootstrap5'

RECAPTCHA_PUBLIC_KEY = '6LdDMzspAAAAABhHNKa7mjiBoJ9pWcLyDugPNAPm'
RECAPTCHA_PRIVATE_KEY = '6LdDMzspAAAAAEDuHwhHuV66OcQcNdb8EoVmXG9G'

USE_THOUSAND_SEPARATOR = True

DEFAULT_FROM_EMAIL = "no-reply@yolobuilds.org"
SERVER_EMAIL = "webmaster@yolobuilds.org"