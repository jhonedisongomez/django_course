from.base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'postgres',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}


STATIC_URL = '/static/'
STATICFILES_DIR = [BASE_DIR.child('child')]