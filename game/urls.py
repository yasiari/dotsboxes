# -*- coding: utf-8 -*- 

from apps.core.handlers import IndexHandler, CssUiHandler
from apps.player.handlers import LoginHandler, RegisterHandler, LogoutHandler


URLS = (

    # Cores APP url + handler
    (r"/$", IndexHandler),
    (r"/css-ui/$", CssUiHandler),

    # player Urls + Handler
    (r"/login/$", LoginHandler),
    (r"/logout/$", LogoutHandler),
    (r"/register/$", RegisterHandler),
)
