from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from driver.models import Driver, Feedback, HIRE_STATUS
from smart_selects.form_fields import ChainedModelChoiceField, ChainedSelect
from helpers.models import Country, State

User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        error_messages = {
            "username": {"unique": ("This username has already been taken.")}
        }


class DriverForm(forms.ModelForm):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "e.g. +234 234 567 890",
                "pattern": "^\+[\d]{8,20}",
                "title": "Mobile number must start with country code e.g +234",
                "data-msg": "Please enter your phone number",
                "minlength": 8,
            }
        ))

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    # hired_status = forms.HiddenInput()

    class Meta:
        model = Driver
        fields = ['country', 'state', 'phone_number', 'address', 'hired_status']
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
            'hired_status': forms.Select(choices=HIRE_STATUS[0][0],
                        attrs={'class': 'selectpicker form-control', "data-style": "btn-selectpicker",
                       "data-live-search": "true",
                       'title': 'Select State', 'autocomplete': 'off',"readonly": True,})
                            }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'message']
        # widgets = {
        #     'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        # }
