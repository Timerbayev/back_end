from django import forms
from .models import Patients


class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=50)
    birthday = forms.DateTimeField()
    complaints = forms.CharField(max_length=200)
    history = forms.CharField(max_length=200)


class Message(forms.Form):
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': 25, 'rows': 5, 'name': "head"}))
    #person = forms.ModelChoiceField(queryset=)