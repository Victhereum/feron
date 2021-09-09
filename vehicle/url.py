from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.inv_dashboard_view, name='inv-dashboard'),
]
