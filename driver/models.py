from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey

from feron.users.models import User
from helpers.models import Country, State

WEEK_CHOICES = (
    (''),
)

DUES_CHOICES = (
    ('payed', 'Payed'),
    ('Not Payed', 'Not Payed'),
    ('Due', 'Due'),
)

FLAG_CHOICES = (
    ('Yellow Flag', 'Yellow Flag'),
    ('Red flag', 'Red Flag'),
)

HIRE_STATUS = (
    ('Reviewing', 'Reviewing'),
    ('Not hired', 'Not Hired'),
    ('Hired', 'Hired'),
    ('Completed', 'Completed'),
)


class Driver(models.Model):
    # Personal Info
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='Driver')

    # Contact
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='driver_country')
    state = ChainedForeignKey(State, on_delete=models.SET_NULL, null=True, chained_field='country',
                              chained_model_field='country')
    address = models.CharField(max_length=100, blank=False)

    # Documents
    # TODO: Get to know the neccesary documents to take from the driver on order to vet them
    id_card = models.FileField(blank=True, null=True)
    id_card_no = models.CharField(max_length=50, blank=True, null=True)
    guarantors_papers = models.FileField(blank=True, null=True)

    # Other Information
    date_joined = models.DateTimeField(auto_now_add=True)
    hired_status = models.CharField(choices=HIRE_STATUS, default=HIRE_STATUS[0][0], max_length=50)
    hired_date = models.DateField(blank=True, null=True)
    hire_ending = models.DateField(blank=True, null=True)

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
