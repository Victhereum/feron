# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=15, blank=False)  # Make this field unique
    phone_no_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.get_full_name()

class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    date = models.DateTimeField(auto_created=True, default=datetime.now())
