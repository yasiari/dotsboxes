# -*- coding: utf-8 -*- 


from apps.core.handlers import (IndexHandler, CssUiHandler)


URLS = (

    # Cores APP url + handler
    (r"/", IndexHandler),
    (r"/css-ui/", CssUiHandler),

    # Auth Urls + Handler
)
