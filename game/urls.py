# -*- coding: utf-8 -*- 

from apps.core.handlers import IndexHandler, CssUiHandler
from apps.player.handlers import SigninHandler, SignupHandler, LogoutHandler


URLS = (

    # Cores APP url + handler
    (r"/$", IndexHandler),
    (r"/css-ui/$", CssUiHandler),

    # player Urls + Handler
    (r"/signin/$", SigninHandler),
    (r"/logout/$", LogoutHandler),
    (r"/signup/$", SignupHandler),
)
