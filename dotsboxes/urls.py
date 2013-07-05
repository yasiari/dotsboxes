# -*- coding: utf-8 -*- 

from dotsboxes.apps.core.handlers import IndexHandler, CssUiHandler
from dotsboxes.apps.player.handlers import ( SigninHandler, SignupHandler, LogoutHandler,
                                             PlayerEditHandler )

URLS = (

    # Cores APP url + handler
    (r"/$", IndexHandler),
    (r"/css-ui/$", CssUiHandler),

    # player Urls + Handler
    (r"/signin/$", SigninHandler),
    (r"/logout/$", LogoutHandler),
    (r"/signup/$", SignupHandler),
    (r"/player/edit/$", PlayerEditHandler),
)
