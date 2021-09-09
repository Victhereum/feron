from django import forms
from django.contrib.auth.models import User
from . import models


class EnquiryForm(forms.Form):
    class Meta:
        model = models.Enquiry
        fields = ['name', 'email', 'phone_no']
