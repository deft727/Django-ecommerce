import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'rm^8ds7_w+kh2m%2_my$rb!s9-dg)cnqk+95yzfw(asx=-b&gb'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD' : '123456',
        'HOST' : 'localhost',
        'PORT': 5432
    }
}


STATIC_DIR =  os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS =  [STATIC_DIR]
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
