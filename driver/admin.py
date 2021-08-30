from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Feedback

admin.site.register(Driver)
admin.site.register(Feedback)
