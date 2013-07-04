# -*- coding: utf-8 -*- 

from django import forms
from apps.player.models import Player
from apps.player import authenticate


class AccountBaseForm(forms.Form):

    playername = forms.CharField(label="Player", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=128)

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

        return self.cleaned_data
