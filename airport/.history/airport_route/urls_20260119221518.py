from .models import Route
from django.urls import path
from . import views
urlpatterns = [
    path('', views.route_operations, name='route_operations'),
    path('add_airport/', views.add_airport, name='add_airport'),
    path('add_routes_between_airports/', views.add_routes_between_airports, name='add_routes_between_airports'),
]
