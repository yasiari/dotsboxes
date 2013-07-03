# -*- coding: utf-8 -*- 

from apps.core.base_handlers import GameRequestHandler
from apps.player.forms import LoginForm, RegisterForm

class LoginHandler(GameRequestHandler):

    def get(self):
        ctx = {
            "login_form": LoginForm()
        }
        self.render_to_response("login.html", ctx)

    def post(self):
        pass

class RegisterHandler(GameRequestHandler):

    def get(self):
        ctx = {
            "register_form": RegisterForm()
        }
        self.render_to_response("register.html", ctx)

    def post(self):
        pass
