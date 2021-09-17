from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse

from investor import models
from .forms import SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()


def driver_signup_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            driver = form.save()
            driver.is_driver = True
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)


            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "driver/driver-auth-register.html", {"form": form,  "msg": msg, "success": success})


# @login_required(login_url='login')
# def inv_dashboard(request):
#     username = models.Investor.objects.get(user_id=request.user.id)
#     return render(request, 'investor/dashboard-partial.html', {'username': username,})
