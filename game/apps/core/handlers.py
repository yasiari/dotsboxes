# -*- coding: utf-8 -*- 

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class CssUiHandler(RequestHandler):
    def get(self):
        self.render("css_ui.html")
