import os
from ConfigParser import SafeConfigParser

DEBUG = False
config = SafeConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config.read(BASE_DIR + '/.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('production', 'DBNAME'),
        'USER': config.get('production', 'DBUSER'),
        'PASSWORD': config.get('production', 'DBPASSWORD'),
        'HOST': config.get('production', 'DBHOST'),
        'PORT': config.get('production', 'DBPORT'),
    }
}

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]