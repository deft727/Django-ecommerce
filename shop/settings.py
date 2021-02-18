"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url

# import dotenv
# import boto3
# import posixpath



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # Persist sessions to DB
SESSION_COOKIE_AGE = 1209600    
# SESSION_ENGINE = 'postgre.django.sessions'
# SESSION_SERIALIZER = 'postgre.django.sessions.BSONSerializer'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rm^8ds7_w+kh2m%2_my$rb!s9-dg)cnqk+95yzfw(asx=-b&gb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.postgres',
    'mptt',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snowpenguin.django.recaptcha3',
    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    'mainapp.apps.MainappConfig',
    'blog.apps.BlogConfig',
    'specs.apps.SpecsConfig',
    'crispy_forms',
    'storages',
    # "compressor",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

     'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'

# Additional prefix for cache keys
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Cache key TTL in second
CACHE_MIDDLEWARE_SECONDS = 600






ROOT_URLCONF = 'shop.urls'

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
                'mainapp.context_processors.single_well_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecom_db',
        'USER': 'kirill',
        'PASSWORD' : 'devpass1',
        'HOST' : 'localhost',
        'PORT': 5432
    }
}
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', True)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ADMINS = [['Webmaster','zarj09@gmail.com']]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static", "media"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mainapp/static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     # other finders..
#     'compressor.finders.CompressorFinder',
# )



EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'magikmagazin123@gmail.com'
EMAIL_HOST_PASSWORD = 'kirill99121'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD ='tiaxxhsvgnvmjyne'


#S3 BUCKETS CONFIG

# +++++++++  статика амазон +++++++++++++++++ #

# #############################################################################
AWS_ACCESS_KEY_ID = 'AKIAYSVUBCGEK2QQAKNU'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'zarj09-crm-bucket'
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = "us-east-2"

# #############################################################################

# AWS_S3_REGION_NAME = "ap-south-1"

# s3 = boto3.resource('s3')

# s3 = boto3.resource(
#     's3',
#     aws_access_key_id='AKIAYSVUBCGEK2QQAKNU',
#     aws_secret_access_key='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',
#     config=Config(signature_version='s3v4')
# )

'''
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
'''








# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)


# DATABASES = {'default': dj_database_url.parse('postgres://the-just-copied-link-comes-here
# postgres://llhqpawwpotqxl:3e0d05c5087d080f1a402295b9e60243b1e135d6e584594eefff73686dcb44c0@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/dfs02v38447867


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "static/uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# debug toolbar settings
# ----------------------

# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

LIQPAY_PRIVATE_KEY = 'sandbox_HGCiYmFzrKiBzzRqi8T57lsD9BrGAgt6R2x7yqy3'
LIQPAY_PUBLIC_KEY= 'sandbox_i41234761583'


RECAPTCHA_PUBLIC_KEY="6Ld9uFAaAAAAAL4iJ255a0SzQzn6gONzvbv_Gz5N"
RECAPTCHA_PRIVATE_KEY="6Ld9uFAaAAAAAEpPN_FuHfFbW1yS6_b410sXgoQs"
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR,'django_cache'),
    }
}



django_heroku.settings(locals())





    # <link href="{% static 'favicon/apple-touch-icon.png'%}" rel="apple-touch-icon">
    # <link href="{% static 'favicon/favicon.png'%}" rel="icon">