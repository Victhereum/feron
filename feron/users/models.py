from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_driver = False
    is_investor = False

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
