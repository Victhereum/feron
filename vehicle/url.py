from django.urls import path
from . import views

urlpatterns = [
    # Investor Vehicle
    path('inv-dashboard/', views.inv_dashboard_view, name='inv-dashboard'),
    path('accounting/', views.inv_accounting, name='inv-accounting'),

    # Driver Vehicle
    path('driver-dashboard/', views.dri_dashboard_view, name='dri-dashboard'),
]
