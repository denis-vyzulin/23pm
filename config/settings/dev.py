from .base import *


# Important variables
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'django-insecure--l1$rq9iw_kvoasf#dst7zjv8*-87e2om&pb0@%@c6&g+)7znd'


# Application definition
WSGI_APPLICATION = 'config.wsgi.application'


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'pm23/assets/',
]
