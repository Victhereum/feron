from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey

from feron.users.models import User
from helpers.models import Country, State


class Investor(models.Model):
    # Personal Info
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investor')
    # The user class provides AUTH data for username, First Name, Last Name, Phone No, and Email
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = ChainedForeignKey(State, on_delete=models.SET_NULL, null=True, chained_field='country',
                              chained_model_field='country')
    address = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    # Bank Account Info
    acc_name = models.CharField(max_length=50, blank=False)
    acc_no = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=50, blank=False)

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Investor.objects.create(user=instance)
    #     instance.investor.save()

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
