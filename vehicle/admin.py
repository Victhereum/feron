from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VehicleType, VehicleInfo, DriverVehicle, InvestorVehicle, Accounting

admin.site.register(VehicleType)
admin.site.register(VehicleInfo)
admin.site.register(DriverVehicle)
admin.site.register(InvestorVehicle)
admin.site.register(Accounting)
