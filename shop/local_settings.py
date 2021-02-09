import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = 'rm^8ds7_w+kh2m%2_my$rb!s9-dg)cnqk+95yzfw(asx=-b&gb'

DEBUG = False



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'