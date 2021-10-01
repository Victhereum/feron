from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from feron.users.models import User
from feron.users.tokens import account_activation_token
from .forms import SignUpForm, DriverForm


def activation_sent_view(request):
    return render(request, 'account/verification_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.email_verified = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse('dri-dashboard'))
    else:
        return render(request, 'account/account_inactive.html')


def driver_signup_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        driver_form = DriverForm(request.POST)
        if form.is_valid() and driver_form.is_valid():
            user = form.save()

            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")

            user.is_active = False
            user.save()

            # Add the user to the DRIVERS group
            dg = Group.objects.get_or_create(name='DRIVERS')
            dg[0].user_set.add(user)
            user.refresh_from_db()

            # Save the User as a driver
            driver = driver_form.save(commit=False)
            driver.user = user
            driver.save()

            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'

            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('account/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),

                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('driver:activation_sent')

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
        driver_form = DriverForm()

    return render(request, "driver/driver-auth-register.html",
                  {"form": form, 'driver': driver_form, "msg": msg, "success": success})
