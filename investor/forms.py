from django.db import transaction

from .models import Investor, Feedback
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter your first name"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter your last name"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter a valid username"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter a valid email address"
            }
        ))
    password1 = forms.CharField(
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter the same password as the one above"
            }
        ))

    # Investor Fields
    phone_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    acc_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    acc_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    bank_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'phone_no', 'country', 'state', 'address',
                  'acc_name', 'acc_no', 'bank_name')

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_investor = True
    #     user.save()
    #     investor = Investor.objects.create(user=user)
    #     return user
