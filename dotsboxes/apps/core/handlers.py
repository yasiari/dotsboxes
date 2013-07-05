# -*- coding: utf-8 -*- 

from dotsboxes.utils.base_handlers import GameRequestHandler, SigninRequireHandler


class IndexHandler(SigninRequireHandler):
    def get(self):
        self.render_to_response("index.html", {})


class CssUiHandler(GameRequestHandler):
    def get(self):
        self.render_to_response("css_ui.html", {})
