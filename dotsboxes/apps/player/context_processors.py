# -*- coding: utf-8 -*- 

from dotsboxes.apps.player.models import AnonymousPlayer


def player(handler_self):
    context = {
    
        "player": AnonymousPlayer()
    }
    
    if handler_self.is_authenticate:
        context["player"] = handler_self.get_current_player()

    return context
