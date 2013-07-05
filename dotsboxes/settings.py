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
AUTOESCAPE = None


# Change setting_locale.py 
COOKIE_SECRET = "61oETzKXQAGaYdkL1hEmGeJJFuYh7EQnp2XdTP1o"


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
    'dotsboxes.apps.player',
)

CONTEXT_PROCESSORS = (
    "dotsboxes.apps.core.context_processors.core",
    "dotsboxes.apps.player.context_processors.player",
)


STATUS_CODE_HTML = {

    "404": "404.html",
    "500": "500.html",
}

UI_MODULES = (
    'dotsboxes.apps.core.ui_modules',
    'dotsboxes.apps.player.ui_modules',  
)


# Settings locale
try:
    from settings_locale import *
except:
    pass


CONF = dict(
    
    ADMINS=ADMINS, 
    DATABASES=DATABASES, 
    INSTALLED_APPS=INSTALLED_APPS,
)

# CONFIGURE
settings.configure(**CONF)
