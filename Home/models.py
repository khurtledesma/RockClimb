from django.db import models

# Create your models here.
class Climbs(models.Model):
    BOULDER = 'B'
    SPORT_CLIMB = "SC"
    TYPES_OF_CLIMBS = [
        (BOULDER, 'Boulder'),
        (SPORT_CLIMB, 'Sport Climb'),
    ]
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=2, default="TX")
    city = models.CharField(max_length=20, default="Austin")
    rating = models.CharField(max_length=5, default='v0')
    typeOfClimb = models.CharField(
        max_length=2,
        choices=TYPES_OF_CLIMBS,
    )
    completed = models.BooleanField(default=True)