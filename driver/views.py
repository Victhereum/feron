from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse

from investor import models
from .forms import SignUpForm, DriverForm
from django.contrib.auth import get_user_model
from driver.models import Driver

User = get_user_model()


# def driver_signup_view(request):
#     msg = None
#     success = False
#
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             driver = form.save()
#
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#             g = Group.objects.get_or_create(name='DRIVERS')
#             g[0].user_set.add(user)
#
#             msg = 'User created - please <a href="/login">login</a>.'
#             success = True
#
#             return redirect("login")
#
#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()
#
#     return render(request, "driver/driver-auth-register.html", {"form": form,  "msg": msg, "success": success})


# @login_required(login_url='login')
# def inv_dashboard(request):
#     username = models.Investor.objects.get(user_id=request.user.id)
#     return render(request, 'investor/dashboard-partial.html', {'username': username,})

def driver_signup_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        driver_form = DriverForm(request.POST)
        if form.is_valid() and driver_form.is_valid():

            driver = form.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            g = Group.objects.get_or_create(name='DRIVERS')
            g[0].user_set.add(user)
            user.refresh_from_db()

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            driver = driver_form.save(commit=False)
            driver.user = user
            driver.save()


            # Driver.country. = driver_form.cleaned_data.get('country')
            # state = driver_form.cleaned_data.get('state')



            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
        driver_form = DriverForm()

    return render(request, "driver/driver-auth-register.html", {"form": form, 'driver': driver_form,  "msg": msg, "success": success})
