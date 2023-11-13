from django.db import models
from django.contrib.auth.models import User


# SQL's
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False)
    lon = models.FloatField()
    lat = models.FloatField()
    type = models.CharField(max_length=20)
    engine = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    year_of_prod = models.IntegerField()
    mileage = models.CharField(max_length=15)
    hometown = models.CharField(max_length=30)                  # from ""
    currently_in = models.CharField(max_length=30)              # currently in ""
    users = models.ManyToManyField(User)                        # чтобы лайкнуть car


class Image(models.Model):
    Image = models.ImageField(upload_to='vehicle_images')
