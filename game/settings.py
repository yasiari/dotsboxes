# -*- coding: utf-8 -*- 

from os.path import abspath, join, dirname


DEBUG = True
PORT = 6969

PROJECT_DIR = abspath(dirname(__file__))
STATIC_DIRECTORY = join(PROJECT_DIR, "static/")


SETTINGS = dict(
    
    debug = DEBUG,
    static_path = STATIC_DIRECTORY,
)
