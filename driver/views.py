from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.db.models import Q


# Driver Sign Up View
def driver_signup_view(request):
    driverUserForm = forms.DriverUserForm()
    driverForm = forms.DriverForm()
    driverDict = {'driverUserForm': driverUserForm, 'driverForm': driverForm}
    if request.method == 'POST':
        driverUserForm = forms.DriverUserForm(request.POST)
        driverForm = forms.DriverForm(request.POST, request.FILES)
        if driverUserForm.is_valid() and driverForm.is_valid():
            user = driverUserForm.save()
            user.set_password(user.password)
            user.save()
            driver = driverForm.save(commit=False)
            driver.user = user
            driver.save()
            driver_group = Group.objects.get_or_create(name='DRIVERS')
            driver_group[0].user_set.add(user)
        return HttpResponseRedirect('driverlogin')
    return render(request, 'driver-auth-register.html', context=driverDict)


# Checking if its a driver
def is_driver(user):
    return user.groups.filter(name='DRIVERS').exists()
