from django.urls import path
from . import views

urlpatterns = [
    path('inv-dashboard/', views.inv_dashboard_view, name='inv-dashboard'),
    path('accounting/', views.inv_accounting, name='inv-accounting'),
]
