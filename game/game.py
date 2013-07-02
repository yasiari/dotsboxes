# -*- coding: utf-8 -*- 

from settings import *
from wsgiref import simple_server
from tornado import wsgi
from urls import URLS


# Handlers Application
application = wsgi.WSGIApplication(URLS, 

    debug = DEBUG,
    static_path = STATIC_DIRECTORY
)


if __name__ == "__main__":

    server = simple_server.make_server('', PORT, application)
    server.serve_forever()
     
