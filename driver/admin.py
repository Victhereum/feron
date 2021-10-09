from django.contrib import admin

from .models import Driver, Feedback


class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'hired_status',)


admin.site.register(Driver, DriverAdmin)
admin.site.register(Feedback)
