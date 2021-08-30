from django import forms
from django.contrib.auth.models import User
from . import models


class InvestorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class InvestorForm(forms.ModelForm):
    class Meta:
        model = models.Investor
        fields = ['country', 'state', 'phone_no']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['name', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }
