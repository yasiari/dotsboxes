# -*- coding: utf-8 -*- 

from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import (check_password, make_password)


class User(models.Model):
    """
        Users Model 
    """
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("password", max_length=128)
    email = models.EmailField("Email", blank=True)
    is_active = models.BooleanField("Active", default=True)
    date_joined = models.DateTimeField("Date Joined", default=timezone.now)
    last_login = models.DateTimeField("last login", default=timezone.now)

    class Meta:
        app_label = "auth"
        db_table = "user"

    def __unicode__(self):
        return u"%s" %(self.username)

    def check_password(self, password):
        return check_password(password, self.password)

    def set_password(self, password):
        self.password = make_password(password)


class Profile(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField("First Name", max_length=30, blank=True)
    last_name = models.CharField("Last Name", max_length=30, blank=True)

    class Meta:
        app_label = "auth"
        db_table = "profile"

    def __unicode__(self):
        return u"%s" %(self.first_name)
