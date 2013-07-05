# -*- coding: utf-8 -*- 

from dotsboxes.utils.base_handlers import ( SuccessRequireHandler, SigninRequireHandler,
                                            SuccessRequireFormHandler, SigninRequireFormHandler )
from dotsboxes.apps.player.forms import SigninForm, SignupForm, PlayerEditForm
from dotsboxes.apps.player.models import Player


class SigninHandler(SuccessRequireFormHandler):
    template = "signin.html"
    form = SigninForm

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)
        self.signin(playername=playername, password=password)

class SignupHandler(SuccessRequireFormHandler):
    template = "signup.html"
    form = SignupForm

    def is_valid(self, data):
        playername = data.get("playername", None)
        password = data.get("password", None)
        email = data.get("email", None)

        # New save player
        player = Player(playername=playername)
        player.password = password
        player.email = email
        player.save()

        # create profile and login
        player.profile_set.create()
        self.signin(playername=playername, password=password, redirect_page="/player/edit/")

class PlayerEditHandler(SigninRequireFormHandler):
    template = "player_edit.html"
    form = PlayerEditForm

    def initial(self):
        player = self.get_current_player()
        profile = player.get_profile()
        return {
            "playername": player.playername,
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "email" : player.email
        }

    def is_valid(self, data):
        player = self.get_current_player()
        profile = player.get_profile()
       
        if bool(data.get("password")):
            player.password = data.get("password")
        player.email = data.get("email")
        player.save()

        profile.first_name = data.get("first_name")
        profile.last_name = data.get("last_name")
        profile.save()

        self.redirect("/player/edit/?status=ok")

class LogoutHandler(SigninRequireHandler):
    def get(self):
        self.clear_cookie("player")
        self.redirect("/signin/")
