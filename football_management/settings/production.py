from .base import *

SECRET_KEY = 'env_val'

DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000/",
]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# SHOULD BE POSTGRES!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}