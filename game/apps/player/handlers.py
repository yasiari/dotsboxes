# -*- coding: utf-8 -*- 

from apps.core.base_handlers import ( SuccessRequireHandler, LoginRequireHandler,
                                     SuccessRequireFormHandler)
from apps.player.forms import LoginForm, RegisterForm
from apps.player import authenticate


class LoginHandler(SuccessRequireFormHandler):

    template = "login.html"
    form = LoginForm

    def get(self):
        ctx = {
            "form": LoginForm()
        }

        self.render_to_response("login.html", ctx)

    def is_valid(self):
        playername = self.get_argument("playername", default=None)
        password = self.get_argument("password", default=None)
        
        auth = authenticate(playername=playername, password=password)
        
        if auth:
            self.set_secure_cookie("player", playername)
            self.redirect("/")
        else:
            self.clear_cookie("player")


class RegisterHandler(SuccessRequireFormHandler):

    template = "register.html"
    form = RegisterForm

    def get(self):
        ctx = {
            "form": RegisterForm()
        }
        self.render_to_response("register.html", ctx)


    def is_valid(self):
        pass


class LogoutHandler(LoginRequireHandler):
    def get(self):
        self.clear_cookie("player")
        self.redirect("/login/")
