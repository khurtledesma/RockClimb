from django.contrib import admin
from django.db import models
from django.utils import timezone

# Register your models here.

class Climbs(models.Model):
    BOULDER = 'B'
    SPORT_CLIMB = "SC"
    TYPES_OF_CLIMBS = [
        (BOULDER, 'Boulder'),
        (SPORT_CLIMB, 'Sport Climb'),
    ]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    typeOfClimb = models.CharField(
        max_length=2,
        choices=TYPES_OF_CLIMBS,
    )
    