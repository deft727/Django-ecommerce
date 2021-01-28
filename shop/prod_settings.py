import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'rm^8ds7_w+kh2m%2_my$rb!s9-dg)cnqk+95yzfw(asx=-b&gb'

DEBUG = False
ALLOWED_HOSTS = ["mysite123456.herokuapp.com"]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'shop',
#         'USER': 'postgres',
#         'PASSWORD' : '123456',
#         'HOST' : 'localhost',
#         'PORT': 5432
#     }
# }



STATIC_DIR =  os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS =  os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'