from django.test import TestCase
from.models import *

# Create your tests here.
class Testing(TestCase):
    def setUp(self):
        a1 = Airport(city = "testcity1", code = "test1")
        a2 = Airport(city = "testcity2", code = "test2")

        f1 = Flight(origin = a1, destination = a2, duration = 100)
        f2 = Flight(origin = a1, destination = a1, duration = 100)
        f3 = Flight(origin = a1, destination = a2, duration = -100)
    
    def test_valid_flight(self):
        a1 = Airport(city = "testcity1", code = "test1")
        a2 = Airport(city = "testcity2", code = "test2")
        flights = Flight.objects.all()
        f2 = Flight(origin = a1, destination = a2, duration = 100)
        self.assertTrue(f2.is_valid_flight())
        