# -*- coding: utf-8 -*- 

from tornado.web import RequestHandler
from apps.core.utils import request_context

class GameRequestHandler(RequestHandler):
    """
        Base Game Handler Class
        in context render_to_response
    """
    def render_to_response(self, template_name, context):
        ctx = request_context()
        context.update(ctx)
        self.render(template_name, **context)

class LoginRequireHandler(GameRequestHandler):
    """
        Login Require Class Redirect not login
    """
    pass

