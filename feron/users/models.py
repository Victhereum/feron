from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.get_full_name()

class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
