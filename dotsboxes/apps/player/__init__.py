# -*- coding: utf-8 -*- 

from dotsboxes.apps.player.models import Player


def authenticate(playername=None, password=None):
    """
        player check password return Player
        authenticate(playername=playername, password=password) 
    """
    try:
        player = Player.objects.get(playername=playername, is_active=True)
    except:
        player = None
    else: 
        if player and player.check_password(password):
            return player
    return None
