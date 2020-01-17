from django import forms
from .models import Users


class Signup(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean_username(self):
        login = self.cleaned_data['username']
        return login

    def save(self):
        users = Users(**self.cleaned_data)
        users.save()


class Log(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        return password


