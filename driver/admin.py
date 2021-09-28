from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Feedback


class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'phone_number', 'hired_status', 'email_verified')


admin.site.register(Driver, DriverAdmin)
admin.site.register(Feedback)
