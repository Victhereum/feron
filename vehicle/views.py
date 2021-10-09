from django.shortcuts import render

from driver.models import Driver
from feron.users.decorators import driver_phone_verification_required
from feron.users.views import is_driver, is_investor
from investor.models import Investor
from .models import InvestorVehicle, DriverVehicle, Accounting


def inv_dashboard_view(request):
    username = Investor.objects.get(user_id=request.user.id)
    user_is_investor = is_investor(request.user)
    inv_vehicles = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related('vehicle')
    info = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related \
        ('vehicle__type__vehicleinfo_set').values \
        ('vehicle__interest_amount', 'vehicle__paid_so_far', 'vehicle__make', 'vehicle__plate_no',
         'vehicle__hired_date', 'vehicle__status')
    # proj_amount = InvestorVehicle.objects.filter\
    #     (investor__user_id=request.user.id).prefetch_related\
    #     ('vehicle__type__vehicleinfo_set').annotate(amount=Sum('vehicle__interest_amount'))

    # vehicles_amount = InvestorVehicle.objects.filter(vehicle__interest_amount=)

    print(user_is_investor)
    dic = {
        'investor': user_is_investor,
        'username': username,
        'inv_vehicles': inv_vehicles,
        'info': info,
        # 'proj_amount': proj_amount
    }
    return render(request, 'investor/inv-dashboard.html', context=dic)


def inv_accounting(request):
    username = Investor.objects.get(user_id=request.user.id)
    user_is_investor = is_investor(request.user)
    record = Accounting.objects.filter(investor__investor__user_id=request.user.id).prefetch_related(
        'investor__vehicle__DriverAssignedVehicle').values(
        'investor__vehicle', 'investor__vehicle__make', 'investor__vehicle__paid_so_far',
        'investor__vehicle__interest_amount', 'investor__vehicle__plate_no', 'date', 'status')

    print(record)

    data = {
        'investor': user_is_investor,
        'username': username,
        'record': record,
    }
    return render(request, 'investor/investor-accounting.html', context=data)


# @login_required
@driver_phone_verification_required
def dri_dashboard_view(request):
    username = Driver.objects.get(user_id=request.user.id)
    user_is_driver = is_driver(request.user)
    dri_vehicle = DriverVehicle.objects.filter(driver__user_id=request.user.id).prefetch_related('vehicle')
    details = DriverVehicle.objects.filter \
        (driver__user_id=request.user.id).values(
        'driver__hired_date', 'vehicle__plate_no',
        'vehicle__model', 'vehicle__make', 'driver__hired_status', 'vehicle__type__type',
        'driver__hire_ending')

    print(details)

    data = {
        'driver': user_is_driver,
        'username': username,
        'dri_vehicle': dri_vehicle,
        'details': details
    }
    return render(request, 'driver/dri-dashboard.html', context=data)


def dri_accounting_view(request):
    username = Driver.objects.get(user_id=request.user.id)
    user_is_driver = is_driver(request.user)
    records = Accounting.objects.filter(driver__driver__user_id=request.user.id).prefetch_related(
        'investor__vehicle__DriverAssignedVehicle').values(
        'investor__vehicle__left_to_pay', 'investor__vehicle__paid_so_far', 'date', 'status'
    )

    tenure = Accounting.objects.filter(driver__driver__user_id=request.user.id).prefetch_related(
        'investor__vehicle__DriverAssignedVehicle').values_list('status')

    payed__so_far = Accounting.objects.filter(driver__driver__user_id=request.user.id).prefetch_related(
        'investor__vehicle__DriverAssignedVehicle').values('investor__vehicle__paid_so_far').get()

    # payed = 0
    # for payed_status in tenure:
    #     # count = payed_status.count
    #     if payed_status == payed_status[0]:
    #         payed = payed + 1
    #
    # status = payed
    print(payed__so_far)
    data = {
        'tenure': tenure,
        'driver': user_is_driver,
        'username': username,
        'records': records,
    }
    return render(request, 'driver/dri-accounting.html', context=data)
