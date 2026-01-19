from .models import Route
from django.urls import path
from . import views
urlpatterns = [
    path('', views.route_operations, name='route_operations'),
    path('add_airport/', views.add_airport, name='add_airport'),
    path()
]
