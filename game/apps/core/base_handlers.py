# -*- coding: utf-8 -*- 

from tornado.web import RequestHandler
from apps.core.utils import request_context, request_data_field
from apps.player.models import Player


class GameRequestHandler(RequestHandler):
    """
        Base Game Handler Class
        in context render_to_response
    """
    def render_to_response(self, template_name, context):
        ctx = request_context()
        context.update(ctx)
        self.render(template_name, **context)

    @property
    def is_authenticate(self):
        return self.get_current_player()

    def get_current_player(self):
        playername = self.get_secure_cookie("player")
        if playername:
            player = Player.objects.get(playername=playername)
            return player
        return None


class BaseFormHandler(GameRequestHandler):
    """
        FormHandler Base Form Class
    """
    form = None
    template = None

    def is_valid(self):
        pass

    def post(self):
        data = request_data_field(self.request, self.form)

        ctx = {}
        form = self.form(data=data)
        
        if form.is_valid():

            self.is_valid()
        else:
            ctx["form"] = form
            self.render_to_response(self.template, ctx)


class LoginRequireHandler(GameRequestHandler):
    """
        Login Require Class Redirect not login
    """
    def prepare(self):
        if self.is_authenticate is None:
            self.redirect("/login/")


class SuccessRequireHandler(GameRequestHandler):
    """
        Success Require Class Redirect not login
    """
    def prepare(self):
        if not self.is_authenticate is None:
            return self.redirect("/")


class LoginRequireFormHandler(LoginRequireHandler, BaseFormHandler):
    """
        FormHandler Login Required
    """
    pass


class SuccessRequireFormHandler(SuccessRequireHandler, BaseFormHandler):
    """
        FormHandler Success Required
    """
    pass
