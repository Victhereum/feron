from django import forms
from django.contrib.auth.models import User
from . import models


class EnquiryForm(forms.Form):
    class Meta:
        model = models.Enquiry
        fields = ['name', 'email', 'phone_no']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
