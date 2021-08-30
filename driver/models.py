from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from feron.users.models import User

WEEK_CHOICES = (
    (''),
)

DUES_CHOICES = (
    ('payed', 'Payed'),
    ('not payed', 'Not Payed'),
    ('due', 'Due'),
)

FLAG_CHOICES = (
    ('Yellow Flag', 'Yellow Flag'),
    ('red flag', 'Red Flag'),
)

HIRE_STATUS = (
    ('not hired', 'Not Hired'),
    ('Hired', 'Hired'),
    ('completed', 'Completed'),
)


class Driver(models.Model):
    # Personal Info
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='Driver')

    # Contact
    phone_number = models.CharField(max_length=15, blank=False, unique=True)
    country = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=100, blank=False)

    # Documents
    # TODO: Get to know the neccesary documents to take from the driver on order to vet them
    # Other Information
    date_joined = models.DateTimeField(auto_now_add=True)
    hired_status = models.CharField(choices=HIRE_STATUS, max_length=50)
    hired_date = models.DateTimeField()
    hire_ending = models.DateTimeField()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.user.username})

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ['date_joined']


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['date']
