# -*- coding: utf-8 -*- 

from wsgiref import simple_server
from tornado import wsgi
from settings import *
from urls import URLS


# Handlers Application
application = wsgi.WSGIApplication(URLS, **SETTINGS)


if __name__ == "__main__":

    server = simple_server.make_server('', PORT, application)
    server.serve_forever()
     
