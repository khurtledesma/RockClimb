from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,  name='index'),
    path('climbs/', views.climbs, name='climbs'),
    path('newClimb/', views.newClimb, name="new_climb"),
    path('routeFinder/', views.routeFinder, name="route_finder"),

]            