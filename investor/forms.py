from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Investor

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
        # min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        max_length=30,
        # min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "data-msg": "Please enter the same password as the one above"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

        error_messages = {
            "username": {"unique": ("This username has already been taken.")}
        }


class InvestorForm(forms.ModelForm):
    # phone_no = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "e.g. +234 234 567 890",
    #             "pattern": "^\+[\d]{8,20}",
    #             "title": "Mobile number must start with country code e.g +234",
    #             "data-msg": "Please enter your phone number",
    #             "minlength": 8,
    #         }
    #     ))

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
        model = Investor
        fields = ['country', 'state', 'address', 'acc_name', 'acc_no', 'bank_name']
        widgets = {
            'country': forms.Select(
                attrs={
                    'class': 'selectpicker form-control', "data-style": "btn-selectpicker", "data-live-search": "true",
                    'title': 'Select Country', 'autocomplete': 'off'}),

            'state': forms.Select(
                # TODO: Set state to ChainedSelect in order to display cities in a particular country
                #  to_app_name='helpers', to_model_name='location', chained_field='country',
                #  chained_model_field='country', foreign_key_app_name='helpers', foreign_key_model_name='State',
                #  foreign_key_field_name='name', show_all=True, auto_choose=False,
                attrs={'class': 'selectpicker form-control', "data-style": "btn-selectpicker",
                       "data-live-search": "true",
                       'title': 'Select State', 'autocomplete': 'off'}),
        }

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_investor = True
    #     user.save()
    #     investor = Investor.objects.create(user=user)
    #     return user
