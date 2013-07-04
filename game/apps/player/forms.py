# -*- coding: utf-8 -*- 

from django import forms
from django.forms.util import ErrorList
from apps.player.models import Player
from apps.player import authenticate
from apps.core.utils import get_or_None

class AccountBaseForm(forms.Form):

    playername = forms.CharField(label="Player", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=128, min_length=6)

    def __init__(self, *args, **kwargs):
        super(AccountBaseForm, self).__init__(*args, **kwargs)
        # PlaceHolder
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs = { 'placeholder': field.label }


class LoginForm(AccountBaseForm):

    def clean(self):
        playername = self.cleaned_data.get('playername')
        password = self.cleaned_data.get('password')

        if playername and password:
            auth = authenticate(playername=playername, password=password)
            if auth is None:
                raise forms.ValidationError("Please enter a correct username and password")

        return self.cleaned_data


class RegisterForm(AccountBaseForm):
    email = forms.EmailField(label="Email")

    def clean(self):
        playername = self.cleaned_data.get('playername')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get("email")

        playername_exists = get_or_None(Player, playername=playername)
        email_exists = get_or_None(Player, email=email)

        if playername_exists:
            self._errors['playername'] = ErrorList(["Player Name already"])

        if email_exists:
            self._errors["email"] = ErrorList(["Player Email already"])
       
        # New player
        if playername_exists is None and email_exists is None:
            player = Player(playername=playername)
            player.password = password
            player.email = email
            player.save()

            # create profile
            player.profile_set.create()

        return self.cleaned_data
