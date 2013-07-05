# -*- coding: utf-8 -*- 

from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import (check_password, make_password)


class Player(models.Model):
    """
        Player Model 
    """
    playername = models.CharField(u"Player", max_length=30, unique=True)
    password = models.CharField(u"Password", max_length=128)
    email = models.EmailField("Email", blank=True)
    is_active = models.BooleanField(u"Active", default=True)
    date_joined = models.DateTimeField(u"Date Joined", default=timezone.now)
    last_login = models.DateTimeField(u"Last login", default=timezone.now)

    class Meta:
        app_label = "player"
        db_table = "player"

    def __unicode__(self):
        return u"%s" %(self.playername)

    def get_profile(self):
        try:
            profile = self.profile_set.get()
        except:
            profile = None
        else:
            if profile is None:
                self.profile_set.create()
        return self.profile_set.get()

    def is_authenticated(self):
        """
            Always return True. This is a way to tell if the user has been
            authenticated in templates.
        """
        return True

    def check_password(self, password):
        return check_password(password, self.password)

    def set_password(self, password):
        self.password = make_password(password)

    def save(self, *args, **kwargs):
        if self.pk is None:
            pass
        self.password = make_password(self.password)
        super(Player, self).save(*args, **kwargs)


class Profile(models.Model):
    player = models.ForeignKey(Player)
    first_name = models.CharField("First Name", max_length=30, blank=True)
    last_name = models.CharField("Last Name", max_length=30, blank=True)

    class Meta:
        app_label = "player"
        db_table = "profile"

    def __unicode__(self):
        return u"%s" %(self.first_name)


class AnonymousPlayer(object):
    """
        AnonymousPlayer Player Model Base
    """
    id = None
    pk = None
    playername = ''
    is_active = False

    def __init__(self):
        pass

    def __str__(self):
        return 'AnonymousPlayer'

    def is_authenticated(self):
        return False

