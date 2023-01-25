from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from. import models

# Create your views here.
def index(request):
    flights_all = models.Flight.objects.all()
    context = {"flights_all": flights_all}
    return render(request, "index.html", context)

def flight_details(request, f_id):
    flight_specific = models.Flight.objects.get(pk = f_id)
    passengers = models.Passengers.objects.filter(flights_related = flight_specific)
    non_passengers = models.Passengers.objects.exclude(flights_related = flight_specific).all()
    context = {"flight_specific":flight_specific, "passengers": passengers, "non_passengers": non_passengers}
    return render(request, "details.html", context)

def register(request, f_id):
    flight_specific = models.Flight.objects.get(pk = f_id)
    passenger_id = request.POST.get("non_p")
    non_passenger = models.Passengers.objects.get(pk = passenger_id)
    non_passenger.flights_related.add(flight_specific)
    return HttpResponseRedirect(reverse('flights:flight_details', args = (f_id,)))
    

def test(request):
    return HttpResponse("Test")
