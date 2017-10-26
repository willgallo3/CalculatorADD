import os
from ConfigParser import SafeConfigParser

DEBUG = False
config = SafeConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config.read(BASE_DIR + '/.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('staging', 'DBNAME'),
        'USER': config.get('staging', 'DBUSER'),
        'PASSWORD': config.get('staging', 'DBPASSWORD'),
        'HOST': config.get('staging', 'DBHOST'),
        'PORT': config.get('staging', 'DBPORT'),
    }
}

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
