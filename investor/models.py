from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from smart_selects.db_fields import ChainedForeignKey
from django.db import models
from feron.users.models import User
from helpers.models import Country, State

class Investor(models.Model):
    # Personal Info
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investor')
    # The user class provides AUTH data for username, First Name, Last Name and Email
    phone_no = models.CharField(max_length=15, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = ChainedForeignKey(State, on_delete=models.SET_NULL, null=True, chained_field='country', chained_model_field='country')
    address = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    # Bank Account Info
    acc_name = models.CharField(max_length=50, blank=False)
    acc_no = models.CharField(max_length=10, unique=True)
    bank_name = models.CharField(max_length=50, blank=False)
    email_verfied = models.BooleanField(default=False)

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Investor.objects.create(user=instance)
    #     instance.investor.save()

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering =['date_joined']


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['date']
