from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_location')
    state = ChainedForeignKey(State, on_delete=models.SET_NULL, null=True, chained_field='country',
                              chained_model_field='country')

    def __str__(self):
        return self.state.name
