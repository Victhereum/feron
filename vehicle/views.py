from django.db import connections
from django.db.models.query_utils import Q
from django.shortcuts import render
from investor.models import Investor
from .models import VehicleInfo, InvestorVehicle, DriverVehicle, Accounting


def inv_dashboard_view(request):
    username = Investor.objects.get(user_id=request.user.id)
    # total_vehicles = InvestorVehicle.objects.filter()
    inv_vehicles = InvestorVehicle.objects.filter(investor__user_id=request.user.id).prefetch_related('vehicle')

    dic = {
        'username': username,
        'inv_vehicles': inv_vehicles,
        # 'vehicle': vehicle,
    }
    return render(request, 'investor/dashboard-partial.html', context=dic)
