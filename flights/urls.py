from django.contrib import admin
from django.urls import path
from . import views 

app_name = "flights"

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:f_id>/flight_details', views.flight_details, name = "flight_details"),
    path('<int:f_id>/register', views.register, name = "register"),
    path('test', views.test, name = "test")

]