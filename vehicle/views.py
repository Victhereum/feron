from django.db import connections
from django.db.models.functions import ExtractWeek
from django.shortcuts import render

from driver.models import Driver
from investor.models import Investor
from .models import VehicleInfo, InvestorVehicle, DriverVehicle, Accounting
from django.db.models import Sum


def inv_dashboard_view(request):
    username = Investor.objects.get(user_id=request.user.id)
    inv_vehicles = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related('vehicle')
    info = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related \
        ('vehicle__type__vehicleinfo_set').values \
        ('vehicle__interest_amount', 'vehicle__paid_so_far', 'vehicle__make', 'vehicle__plate_no',
         'vehicle__hired_date', 'vehicle__status')
    # proj_amount = InvestorVehicle.objects.filter\
    #     (investor__user_id=request.user.id).prefetch_related\
    #     ('vehicle__type__vehicleinfo_set').annotate(amount=Sum('vehicle__interest_amount'))

    # vehicles_amount = InvestorVehicle.objects.filter(vehicle__interest_amount=)

    # print(proj_amount)
    dic = {
        'username': username,
        'inv_vehicles': inv_vehicles,
        'info': info,
        # 'proj_amount': proj_amount
    }
    return render(request, 'investor/inv-dashboard.html', context=dic)


def inv_accounting(request):
    username = Investor.objects.get(user_id=request.user.id)
    record = Accounting.objects.filter(investor__investor__user_id=request.user.id).prefetch_related(
        'investor__vehicle__DriverAssignedVehicle').values(
        'investor__vehicle', 'investor__vehicle__make', 'investor__vehicle__paid_so_far',
        'investor__vehicle__interest_amount', 'investor__vehicle__plate_no', 'date', 'status')

    print(record)

    data = {
        'username': username,
        'record': record,
    }
    return render(request, 'investor/investor-accounting.html', context=data)


def dri_dashboard_view(request):
    username = Driver.objects.get(user_id=request.user.id)
    dri_vehicle = DriverVehicle.objects.filter(driver__user_id=request.user.id).prefetch_related('vehicle')
    details = DriverVehicle.objects.filter \
        (driver__user_id=request.user.id).values(
        'driver__hired_date', 'vehicle__plate_no',
        'vehicle__model', 'vehicle__make', 'driver__hired_status', 'vehicle__type__type',
        'driver__hire_ending')

    print(details)

    data = {
        'username': username,
        'dri_vehicle': dri_vehicle,
        'details': details
    }
    return render(request, 'driver/dri-dashboard.html', context=data)

def dri_accounting_view(request):
    username = Driver.objects.get(user_id=request.user.id)
    records = Accounting.objects.filter(driver__driver__user_id=request.user.id).prefetch_related(
        'driver__vehicle__VehiclesInvested').values(
        'investor__vehicle__left_to_pay', 'investor__vehicle__paid_so_far', 'date', 'status'
    )


    data = {
        'username': username,
        'records': records,
    }
    return render(request, 'driver/dri-accounting.html', context=data)
