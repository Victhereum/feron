from django.db import connections
from django.db.models.query_utils import Q
from django.shortcuts import render
from investor.models import Investor
from .models import VehicleInfo, InvestorVehicle, DriverVehicle, Accounting


def inv_dashboard_view(request):
    username = Investor.objects.get(user_id=request.user.id)
    no_of_inv_vehicles = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related('vehicle')
    inv_vehicle = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related('vehicle__type__vehicleinfo_set')

    # vehicles_amount = InvestorVehicle.objects.filter(vehicle__interest_amount=)

    # print(vehicles.query)
    dic = {
        'username': username,
        'inv_vehicles': no_of_inv_vehicles,
        'vehicle': inv_vehicle,
    }
    return render(request, 'investor/dashboard-partial.html', context=dic)
