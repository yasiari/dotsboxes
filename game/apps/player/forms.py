# -*- coding: utf-8 -*- 

from django.forms import ModelForm, Textarea
from apps.player.models import Player

class LoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # PlaceHolder
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs = { 'placeholder': field.label }
    class Meta:
        model = Player
        fields = ["playername", "password"]


class RegisterForm(LoginForm):
    class Meta:
        model = Player
        fields = ["playername", "email", "password"]
