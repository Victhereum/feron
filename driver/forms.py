from django import forms
from feron.users.models import User
from . import models


class DriverUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        # widgets = {
        #     'first_name': forms.CharField(attrs={}),
        #     'last_name': forms.CharField(attrs={'class': 'answer'}),
        #     'username': forms.CharField(attrs={'class': 'answer'}),
        #     'email': forms.EmailInput(attrs={'class': 'answer'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'answer'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'answer'}),
        #         }


class DriverForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = ['country', 'state', 'phone_number']
        # widgets = {
        #     'country': forms.CharField(attrs={'class': 'answer'}),
        #     'state': forms.CharField(attrs={'class': 'answer'}),
        #     'phone_number': forms.CharField(attrs={'class': 'answer'})
        #
        # }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['name', 'message']
        # widgets = {
        #     'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        # }
