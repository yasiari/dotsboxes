# -*- coding: utf-8 -*- 

from apps.core.base_handlers import SuccessRequireHandler
from apps.player.forms import LoginForm, RegisterForm

class LoginHandler(SuccessRequireHandler):

    def get(self):
        ctx = {
            "login_form": LoginForm()
        }
        self.render_to_response("login.html", ctx)

    def post(self):
        pass

class RegisterHandler(SuccessRequireHandler):

    def get(self):
        ctx = {
            "register_form": RegisterForm()
        }
        self.render_to_response("register.html", ctx)

    def post(self):
        pass
