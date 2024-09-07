from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    class TypeRoom(models.TextChoices):
        STANDARD = "STD", "Standart"
        LUXURY =  "LUX",  "Luxury"
        ECONOMY = "ECO", "Econom"
        PRESIDENT = "PRS", "President"

    class TypeBuilding(models.TextChoices):
        HOUSE = "HSE", "House"
        ROOM = "ROM", "Room"

    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    types = models.CharField(max_length=50, choices=TypeRoom.choices)
    type_building = models.CharField(max_length=50, choices=TypeBuilding.choices)

    def __str__(self):
        return self.name, self.price

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user, self.place