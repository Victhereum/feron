# from django.shortcuts import render, redirect
# from django.shortcuts import render, redirect
# from django.contrib import messages, auth
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# from django.urls import reverse
# from . import forms,models
# from django.db.models import Sum
# from django.contrib.auth.models import Group
# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required,user_passes_test
# from django.conf import settings
# from django.db.models import Q


# Investor Sign Up View
# def investor_signup_view(request):
#     investorUserForm=forms.SignUpForm()
#     investorForm=forms.InvestorForm()
#     investorDict={'investorUserForm':investorUserForm,'investorForm':investorForm}
#     if request.method == 'POST':
#         investorUserForm = forms.SignUpForm(request.POST)
#         investorForm=forms.InvestorForm(request.POST,request.FILES)
#         if investorUserForm.is_valid() and investorForm.is_valid():
#             user=investorUserForm.save()
#             user.set_password(user.password)
#             user.save()
#             investor = investorForm.save(commit=False)
#             investor.user = user
#             investor.save()
#             investor_group = Group.objects.get_or_create(name='INVESTORS')
#             investor_group[0].user_set.add(user)
#         return HttpResponseRedirect(reverse('login'))
#     return render(request, 'investor/inv-auth-register.html', context=investorDict)

#
# def is_investor(user):
#     return Investor.user_id.exists()


# # Create your views here.
# def investor_signup_view(request):
#     if request.method == 'POST':
#         # GEt form values
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password1']
#         password2 = request.POST['password2']
#
#         # Check if passwords match
#         if password == password2:
#             # Check username
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, ' username already taken')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, ' email already exist')
#                     return redirect('register')
#                 else:
#                     # Looks Good
#                     user = User.objects.create(username=username, password=password
#                                                , email=email, first_name=first_name, last_name=last_name)
#                     # Login after register()
#                     # auth.login(request, user)
#                     # messages.success(request, 'You are login')
#                     # return redirect('index')
#                     user.save()
#                     messages.success(request, 'You are now registered and can login')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Password do not match')
#             return redirect('inv-signup')
#
#     else:
#         return render(request, 'investor/inv-auth-register.html')

# def profile(request, pk):
#     if request.method == 'POST':
# def register_user(request):
#     msg = None
#     success = False
#
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#
#             msg = 'User created - please <a href="/login">login</a>.'
#             success = True
#
#             # return redirect("/login/")
#
#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()
#
#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
#
# def login(request):
#     if request.method == 'POST':
#         # Login User
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password')
#             return redirect('login')
#     else:
#         return render(request, 'investor/inv-auth-register.html')
#
#
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'You are now logged out')
#         return redirect('index')

# TODO: If this works, then use it through out and delete the others
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse

from investor import models
from .forms import SignUpForm, InvestorForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


def investor_signup_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        investor_form = InvestorForm(request.POST)
        if form.is_valid() and investor_form.is_valid():

            investor = form.save()
            # investor.is_investor = True

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            g = Group.objects.get_or_create(name='INVESTORS')
            g[0].user_set.add(user)
            # user.refresh_from_db()

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            investor = investor_form.save(commit=False)
            investor.user = user
            investor.save()

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
        investor_form = InvestorForm()

    return render(request, "investor/inv-auth-register.html",
                  {"form": form, 'investor': investor_form,  "msg": msg, "success": success})

# @login_required(login_url='login')
# def inv_dashboard(request):
#     username = models.Investor.objects.get(user_id=request.user.id)
#     return render(request, 'investor/dashboard-partial.html', {'username': username,})
