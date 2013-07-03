# -*- coding: utf-8 -*- 

# django settings must be called before importing models
from django.conf import settings
from os.path import abspath, join, dirname

DEBUG = False
PORT = 8888


ADMINS = (
    
    ('yasar icli', 'yasaricli@gmail.com'),   
)


PROJECT_DIR = abspath(dirname(__file__))
STATIC_PATH = join(PROJECT_DIR, "static/")
TEMPLATE_PATH = join(PROJECT_DIR, "templates/")

# Database config && 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'game.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# APPLICATIONS
INSTALLED_APPS = (
    'apps.auth',
)

AUTH_USER_MODEL = "apps.auth.User"


# Settings locale
try:
    from settings_locale import *
except:
    pass


CONF = dict(
    
    ADMINS=ADMINS, 
    DATABASES=DATABASES, 
    INSTALLED_APPS=INSTALLED_APPS,
    AUTH_USER_MODEL = AUTH_USER_MODEL,
)

# CONFIGURE
settings.configure(**CONF)
