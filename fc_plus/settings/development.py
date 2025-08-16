from .base import *

SECRET_KEY = 'django-insecure-f&b+4n6o@v*(_i1=(mw*^%d-!*dhp8j&@#b26fz_v$hbz39ho_'

DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ["Authorization", "Content-Type", "Accept"]
CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SAMESITE = 'none'
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = 'localhost'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}