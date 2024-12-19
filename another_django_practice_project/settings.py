"""
Django settings for another_django_practice_project project.

Generated by 'django-admin startproject' using Django 4.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import pymysql
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9v#h6(mr#z!!pv!&bp%h_o86blmqo))uf*t-rr9zb^3t1v@0#9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'another_django_practice_project',
    'user',
    'article',
    'blog',
    # For Using Django-Allauth (OAuth)
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',  # Example for Google OAuth
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',  # For Using Django-Allauth (OAuth)
]

ROOT_URLCONF = 'another_django_practice_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],         # Leave this empty for app-specific templates
        'APP_DIRS': True,   # Enable discovery of templates in app directories
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

WSGI_APPLICATION = 'another_django_practice_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'another_django_practice_project',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Or the MySQL server's address
        'PORT': '3306',       # Default MySQL port
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',  # Enforce stricter validation
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuration for sending emails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your SMTP provider
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ramandhiman1322@gmail.com'
EMAIL_HOST_PASSWORD = 'Raman@80539'
EMAIL_TIMEOUT = 5  # Optional: Set a timeout for SMTP connections


# MESSAGE_STORAGE configuration
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

LOGIN_URL = '/login/'  # Update to the URL path of your login view
APPEND_SLASH = True   # If you want Django to automatically append slashes to URLs


# For Using a Custom User Model
AUTH_USER_MODEL = 'user.CustomUser'

# Add your custom backend in settings.py for Using an Alternative Model for Authentication
AUTHENTICATION_BACKENDS = [
    'user.backends.CustomAuthBackend',  # Custom backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    # 'allauth.account.auth_backends.AuthenticationBackend',  #for user authentication using OAuth
]

# # Add this to define the site ID for your app
# SITE_ID = 1  # Make sure this is set correctly

# # Social Account settings
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<Your Google Client ID>'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<Your Google Client Secret>'