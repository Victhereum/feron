from django.contrib import admin

from .models import Investor, Feedback


class InvestorAdmin(admin.ModelAdmin):
    list_display = ('user', 'state',)


admin.site.register(Investor, InvestorAdmin)
admin.site.register(Feedback)
