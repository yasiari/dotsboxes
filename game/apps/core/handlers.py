# -*- coding: utf-8 -*- 

from apps.core.base_handlers import GameRequestHandler

class IndexHandler(GameRequestHandler):
    def get(self):
        self.render_to_response("index.html", {})

class CssUiHandler(GameRequestHandler):
    def get(self):
        self.render_to_response("css_ui.html", {})
