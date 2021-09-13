from django.db import models
from investor.models import Investor
from driver.models import Driver
from datetime import datetime

COLORS_CHOICE = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('white', 'White'),
    ('black', 'Black'),
    ('Silver', 'Silver'),
    ('yellow', 'Yellow'),
)

VEHICLE_CHOICES = (
    ('keke', 'Keke'),
    ('taxi', 'Taxi'),
    ('Luxury Cab', 'Luxury Cab'),
)

INSPECTION_CHOICES = (
('good', 'In Good Shape'),
('bad', 'Needs Repairs'),
('repaired', 'Have been Repaired'),
)

VEHICLE_STATUS = (
    ('not hired', 'Not Yet Hired'),
    ('hired', 'Hired'),
    ('completed', 'completed'),
)

PAYMENT_STATUS = (
    ('payed', 'Payed'),
    ('due', 'Due'),
    ('not payed', 'Not Payed'),
    ('completed', 'Completed'),
)

class VehicleType(models.Model):
    type = models.CharField(max_length=150, blank=False, choices=VEHICLE_CHOICES, default=VEHICLE_CHOICES[0][0])

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']

class VehicleInfo(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    make = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=20, blank=False)
    year = models.IntegerField(blank=False)
    color = models.CharField(max_length=20, blank=False, choices=COLORS_CHOICE, default=COLORS_CHOICE[0][0])
    vin = models.CharField(max_length=50, blank=False, unique=True)
    engine_no = models.PositiveBigIntegerField(blank=False, unique=True)
    plate_no = models.CharField(max_length=10, unique=True)
    tracker_imei_no = models.IntegerField(blank=False, unique=True)
    # TODO: get the neccesary detail for the vehicle papers and correct before launching
    vehicle_papers = models.FileField(upload_to='vehicle_papers')
    inspection = models.CharField(max_length=25, blank=False, choices=INSPECTION_CHOICES, default=INSPECTION_CHOICES[0][0])
    inspection_description = models.TextField(max_length=500, blank=False)
    value_at_acquisition = models.IntegerField()
    interest_amount = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=VEHICLE_STATUS)
    weekly_returns = models.IntegerField()
    paid_so_far = models.IntegerField()
    left_to_pay = models.IntegerField()
    # tenure_duration = models.DateField(blank=True)
    hired_date = models.DateField()
    hire_ending = models.DateField()


    def __str__(self):
        return self.plate_no

    class Meta:
        ordering = ['date_created']


class DriverVehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='Driver')
    vehicle = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE, related_name='DriverAssignedVehicle')

    def __str__(self):
        return self.driver.user.email

    class Meta:
        unique_together = ('driver', 'vehicle')


class InvestorVehicle(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='Investor')
    vehicle = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE, related_name='VehiclesInvested')

    def __str__(self):
        return f'{self.investor.acc_name} {self.vehicle.make} {self.vehicle.model}'

    class Meta:
        unique_together = ('investor', 'vehicle')


class Accounting(models.Model):
    driver = models.ForeignKey(DriverVehicle, on_delete=models.CASCADE, related_name='driver_accounting', blank=False)
    investor = models.ForeignKey(InvestorVehicle, on_delete=models.CASCADE, related_name='investor_accounting', blank=False)
    date = models.DateField(unique=True)
    status = models.CharField(choices=PAYMENT_STATUS,  max_length=20)

    def __str__(self):
        return f'{self.driver.driver.user.get_full_name()} {self.investor.investor.user.get_full_name()} {self.status}'

    class Meta:
        ordering = ['date']





