from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.db.models import Q


# Investor Sign Up View
def investor_signup_view(request):
    investorUserForm=forms.InvestorUserForm()
    investorForm=forms.InvestorForm()
    investorDict={'investorUserForm':investorUserForm,'investorForm':investorForm}
    if request.method=='POST':
        investorUserForm=forms.InvestorUserForm(request.POST)
        investorForm=forms.InvestorForm(request.POST,request.FILES)
        if investorUserForm.is_valid() and investorForm.is_valid():
            user=investorUserForm.save()
            user.set_password(user.password)
            user.save()
            investor=investorForm.save(commit=False)
            investor.user=user
            investor.save()
            investor_group = Group.objects.get_or_create(name='INVESTORS')
            investor_group[0].user_set.add(user)
        return HttpResponseRedirect('investorlogin')
    return render(request,'inv-auth-register.html',context=investorDict)


def is_investor(user):
    return user.groups.filter(name='INVESTORS').exists()
