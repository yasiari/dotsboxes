# -*- coding: utf-8 -*- 

from django import forms
from django.forms.util import ErrorList
from dotsboxes.apps.player import authenticate
from dotsboxes.apps.player.models import Player
from dotsboxes.utils import get_or_None

class AccountBaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AccountBaseForm, self).__init__(*args, **kwargs)
        # PlaceHolder
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs = { 'placeholder': field.label, "autocomplete": "off" }

class SigninForm(AccountBaseForm):
    playername = forms.CharField(label="Player", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=128)

    def clean(self):
        playername = self.cleaned_data.get('playername')
        password = self.cleaned_data.get('password')

        if playername and password:
            auth = authenticate(playername=playername, password=password)
            if auth is None:
                raise forms.ValidationError("Please enter a correct username and password")

        return self.cleaned_data

class SignupForm(AccountBaseForm):
    playername = forms.CharField(label="Player Name", max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=128, min_length=6)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        player = get_or_None(Player, email=email)
        if player:
            raise forms.ValidationError("Player Email already")
        return email

    def clean_playername(self):
        playername = self.cleaned_data.get('playername')
        player = get_or_None(Player, playername=playername)
        if player:
            raise forms.ValidationError("Player Name already")
        return playername

class PlayerEditForm(AccountBaseForm):
    playername = forms.CharField(label="Player Name", max_length=30, required=False)
    first_name = forms.CharField(label="First Name", max_length=30, required=False)
    last_name = forms.CharField(label="Last Name", max_length=30, required=False)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=128, min_length=6, required=False)

    def __init__(self, *args, **kwargs):
        super(PlayerEditForm, self).__init__(*args, **kwargs)
        self.fields["playername"].widget.attrs.update({ "readonly": "readonly" })

    def clean_email(self):
        playername = self.cleaned_data.get('playername')
        email = self.cleaned_data.get("email")
        player = get_or_None(Player, email=email)
        if player and not player.playername == playername:
            raise forms.ValidationError("Player Name already")
        return email
        





