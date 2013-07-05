# -*- coding: utf-8 -*-

import sys
import tornado.web


from tornado import wsgi
from wsgiref import simple_server
from django.core.management import execute_from_command_line

from dotsboxes.settings import *
from dotsboxes.urls import URLS
from dotsboxes.utils.base_handlers import RequestErrorHandler
from dotsboxes.utils import ui_modules


class BaseCommandBackend(object):
    """
        python sys.argv

        sample:
            python dotsboxes.py startgame
            python dotsboxes.py django [commands] sql, shell bla bla
    """
    PORT = PORT
    DEBUG = DEBUG
    URLS  = URLS 
    STATIC_PATH = STATIC_PATH
    TEMPLATE_PATH = TEMPLATE_PATH
    AUTOESCAPE = AUTOESCAPE
    COOKIE_SECRET = COOKIE_SECRET

    def __init__(self):

        # Handlers Application
        self.application = wsgi.WSGIApplication(self.URLS, 

            debug = self.DEBUG,
            static_path = self.STATIC_PATH,
            template_path = self.TEMPLATE_PATH,
            autoescape = self.AUTOESCAPE,
            cookie_secret = self.COOKIE_SECRET,
            ui_modules = ui_modules(),
        )
    
    def get_command(self, commands):
        method = getattr(self, commands[1])
        method(commands)



class DotsBoxesCommand(BaseCommandBackend):
    """
        django, startgame command
    """
    def django(self, commands):
        del commands[1]
        execute_from_command_line(commands)

    def startgame(self, commands):

        ## override the tornado.web.ErrorHandler with our default RequestErrorHandler
        tornado.web.ErrorHandler = RequestErrorHandler

        server = simple_server.make_server('', self.PORT, self.application)
        server.serve_forever()
