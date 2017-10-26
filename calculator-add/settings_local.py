import os
import dj_database_url
from ConfigParser import SafeConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = SafeConfigParser()
config.read(BASE_DIR + '/.env')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600),
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
