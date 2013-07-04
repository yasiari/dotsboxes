# -*- coding: utf-8 -*- 

from settings import STATUS_CODE_HTML
from tornado.web import RequestHandler, ErrorHandler, HTTPError
from apps.player import authenticate
from apps.core.utils import request_context, request_data_field, template_loader
from apps.player.models import Player


class GameRequestHandler(RequestHandler):
    """
        Base Game Handler Class
        in context render_to_response

        write_error Production DEBUG False then  render STATUS_CODE_HTML html
    """
    def write_error(self, status_code, **kwargs):
        if self.settings.get("debug") is False:

            ctx = {
                "status_code": status_code,
                "message": self._reason,
            }
            
            template = template_loader(STATUS_CODE_HTML.get(str(status_code)), ctx)
            self.finish(template)
        
        else:
            super(GameRequestHandler, self).write_error(status_code, **kwargs)

    def render_to_response(self, template_name, context):
        ctx = request_context()
        context.update(ctx)
        self.render(template_name, **context)

    @property
    def is_authenticate(self):
        return self.get_current_player()

    def signin(self, playername=None, password=None, redirect_page="/"):
        auth = authenticate(playername=playername, password=password)
        
        if auth:
            self.set_secure_cookie("player", playername)
            self.redirect(redirect_page)
        else:
            self.clear_cookie("player")

    def get_current_player(self):
        playername = self.get_secure_cookie("player")
        if playername:
            player = Player.objects.get(playername=playername)
            return player
        return None


class RequestErrorHandler(ErrorHandler, GameRequestHandler):
    def prepare(self):
        if self.settings.get("debug") is False:
            ctx = {
                "status_code": self._status_code
            }

            self.render_to_response(STATUS_CODE_HTML.get(str(self._status_code)), ctx)
        else:
            # debug true  
            raise HTTPError(self._status_code)


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

            self.is_valid(data)
        else:
            ctx["form"] = form
            self.render_to_response(self.template, ctx)


class SigninRequireHandler(GameRequestHandler):
    """
        Signin Require Class Redirect not signin
    """
    def prepare(self):
        if self.is_authenticate is None:
            self.redirect("/signin/")


class SuccessRequireHandler(GameRequestHandler):
    """
        Success Require Class Redirect not signin
    """
    def prepare(self):
        if not self.is_authenticate is None:
            return self.redirect("/")


class SigninRequireFormHandler(SigninRequireHandler, BaseFormHandler):
    """
        FormHandler Signin Required
    """
    pass


class SuccessRequireFormHandler(SuccessRequireHandler, BaseFormHandler):
    """
        FormHandler Success Required
    """
    pass
