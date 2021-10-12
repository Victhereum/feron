from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Enquiry


class Profile(UserAdmin):
    list_display = ('phone_no', 'phone_no_verified', 'email_verified')


admin.site.register(User, UserAdmin)
admin.site.register(Enquiry)
