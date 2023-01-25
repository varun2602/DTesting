from django.db import models

# Create your models here
class Airport(models.Model):
    city = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10) 

    def __str__(self):
        return f"{self.city}({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "departures")
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "arrivals")
    duration = models.IntegerField(max_length = 5) 

    def __str__(self):
        return f"Flight {self.id}"

    def is_valid_flight(self):
        if self.origin != self.destination and self.duration > 0:
            return True
        else:
            return False

class Passengers(models.Model):
    fname = models.CharField(max_length = 50)
    flights_related = models.ManyToManyField(Flight, blank = True, related_name = "passengers_related") 

    def __str__(self):
        return f"{self.fname}"

