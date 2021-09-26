from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    name = models.CharField(max_length=30)
