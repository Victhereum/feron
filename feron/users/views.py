from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from driver.models import Driver
from investor.models import Investor
from django.contrib.auth.models import Group
from . import forms
from . import models


# for checking if user is either an Investor or a driver
def is_investor(user):
    return user.groups.filter(name='INVESTORS').exists()


def is_driver(user):
    return user.groups.filter(name='DRIVERS').exists()


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')
    enq = forms.EnquiryForm()
    if request.method == 'POST':
        sub = forms.EnquiryForm(request.POST)
        if sub.is_valid():
            name = sub.cleaned_data['Name']
            email = sub.cleaned_data['Email']
            phone_no = sub.cleaned_data['Phone']
            send_mail(str(name) + ' || ' + str(email), str(phone_no), settings.EMAIL_HOST_USER,
                      settings.EMAIL_RECEIVING_USER, fail_silently=False)
            return render(request, 'pages/home.html')
    return render(request, 'pages/home.html', {'form': enq})


def login_view(request):
    form = forms.LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active and user.is_authenticated and is_investor(user):
                    login(request, user)
                    return redirect("inv-dashboard")
                elif user.is_active and user.is_authenticated and is_driver(user):
                    login(request, user)
                    return redirect("dri-dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "account/auth-login.html", {"form": form, "msg": msg})
