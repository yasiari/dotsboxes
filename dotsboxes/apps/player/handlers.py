# -*- coding: utf-8 -*- 

from dotsboxes.utils.base_handlers import ( SuccessRequireHandler, SigninRequireHandler,
                                     SuccessRequireFormHandler)
from dotsboxes.apps.player.forms import SigninForm, SignupForm
from dotsboxes.apps.player.models import Player


class SigninHandler(SuccessRequireFormHandler):

    template = "signin.html"
    form = SigninForm

    def get(self):
        ctx = {
            "form": SigninForm()
        }

        self.render_to_response("signin.html", ctx)

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)

        # signin
        self.signin(playername=playername, password=password)


class SignupHandler(SuccessRequireFormHandler):
    """
        Signup And Signin Form Handler
    """
    template = "signup.html"
    form = SignupForm

    def get(self):
        ctx = {
            "form": SignupForm()
        }
        self.render_to_response("signup.html", ctx)

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)
        email = data.get("email", None)

        # New save player
        player = Player(playername=playername)
        player.password = password
        player.email = email
        player.save()

        # create profile
        player.profile_set.create()

        # signin
        self.signin(playername=playername, password=password)
        

class LogoutHandler(SigninRequireHandler):
    def get(self):
        self.clear_cookie("player")
        self.redirect("/signin/")
