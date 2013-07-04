# -*- coding: utf-8 -*- 

from apps.core.base_handlers import ( SuccessRequireHandler, LoginRequireHandler,
                                     SuccessRequireFormHandler)
from apps.player.forms import LoginForm, RegisterForm


class LoginHandler(SuccessRequireFormHandler):

    template = "login.html"
    form = LoginForm

    def get(self):
        ctx = {
            "form": LoginForm()
        }

        self.render_to_response("login.html", ctx)

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)

        # login
        self.login(playername=playername, password=password)


class RegisterHandler(SuccessRequireFormHandler):
    """
        Register And Login Form Handler
    """
    template = "register.html"
    form = RegisterForm

    def get(self):
        ctx = {
            "form": RegisterForm()
        }
        self.render_to_response("register.html", ctx)

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)

        # login
        self.login(playername=playername, password=password)
        

class LogoutHandler(LoginRequireHandler):
    def get(self):
        self.clear_cookie("player")
        self.redirect("/login/")
