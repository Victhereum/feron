from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Investor, Feedback


class InvestorAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'phone_no', 'email_verfied')


admin.site.register(Investor, InvestorAdmin)
admin.site.register(Feedback)
