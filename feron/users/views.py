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
    enquiry_email = 'enquiry@feronauto.com'
    if request.user.is_authenticated and is_investor(request.user):
        return HttpResponseRedirect('inv-dashboard')
    elif request.user.is_authenticated and is_driver(request.user):
        return HttpResponseRedirect('dri-dashboard')
    else:
        enq = forms.EnquiryForm()
    if request.method == 'POST':
        enquiry = forms.EnquiryForm(request.POST)
        if enquiry.is_valid():
            name = enquiry.cleaned_data['name']
            email = enquiry.cleaned_data['email']
            phone_no = enquiry.cleaned_data['phone_no']
            send_mail(subject='New Enquiry About Feron', message=f'There is a new enquiry about Feron Auto \n\n'
                                                                 f'The message was sent by {name.capitalize()}\n\n'
                                                                 f'With Email "{email}" \n\n'
                                                                 f'and Phone No: {phone_no} \n\n'
                                                                 f'Do well to contact as soon as possible',
                      from_email=None, recipient_list=[enquiry_email], auth_user=None, auth_password=None, fail_silently=False)
            return render(request, 'pages/home.html')
    return render(request, 'pages/home.html', {'form': enq})


def login_view(request):
    form = forms.LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password, username=username)
            if user:
                if user.is_active and user.is_authenticated and is_investor(user):
                    login(request, user)
                    return redirect("inv-dashboard")
                elif user.is_active and user.is_authenticated and is_driver(user):
                    login(request, user)
                    return redirect("dri-dashboard")
                else:
                    msg = 'You are not a Driver nor are you an Investor, Send us an email in order to resolve the issue'
            else:
                msg = 'This Username or Password does not exist, Please try again'
        else:
            msg = 'Error validating the form'

    return render(request, "account/auth-login.html", {"form": form, "msg": msg})
