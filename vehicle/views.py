from django.db import connections
from django.db.models.query_utils import Q
from django.shortcuts import render
from investor.models import Investor
from .models import VehicleInfo, InvestorVehicle, DriverVehicle, Accounting


def inv_dashboard_view(request):
    username = Investor.objects.get(user_id=request.user.id)
    # total_vehicles = InvestorVehicle.objects.filter()
    query = request.GET.get("q", None)
    vehicles = InvestorVehicle.objects.filter(investor_id=request.user.id)
    total_vehicle = [x.vehicle for x in vehicles]
    qs = VehicleInfo.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )
    qs_one = []
    for x in qs:
        if x in total_vehicle:
            qs_one.append(x)
        else:
            pass

    print(vehicles.query)
    # vehicle_make = InvestorVehicle.objects.
    # vehicle_model = InvestorVehicle.vehicle.model
    # vehicle = f'{vehicle_make} {vehicle_model}'
    # print(total_vehicles.query)
    dic = {
        'username': username,
        'total_vehicles': qs_one,
        # 'vehicle': vehicle,
    }
    return render(request, 'investor/dashboard-partial.html', context=dic)
