# -*- coding: utf-8 -*- 

import tornado.web
from settings import *
from wsgiref import simple_server
from tornado import wsgi
from urls import URLS
from apps.core.base_handlers import RequestErrorHandler

# Handlers Application
application = wsgi.WSGIApplication(URLS, 

    debug = DEBUG,
    static_path = STATIC_PATH,
    template_path = TEMPLATE_PATH,
    autoescape = AUTOESCAPE,
    cookie_secret = COOKIE_SECRET,
)

## override the tornado.web.ErrorHandler with our default RequestErrorHandler
tornado.web.ErrorHandler = RequestErrorHandler

if __name__ == "__main__":

    server = simple_server.make_server('', PORT, application)
    server.serve_forever()
     
