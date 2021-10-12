from django import forms
from django.contrib.auth.models import User
from . import models


class EnquiryForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control-input"
            }
        ))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control-input"
            }
        ))
    phone_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone No",
                "class": "form-control-input"
            }
        ))

    class Meta:
        model = models.Enquiry
        fields = ['name', 'email', 'phone_no']


class LoginForm(forms.Form):
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Username",
    #             "class": "form-control"
    #         }
    #     ))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
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
