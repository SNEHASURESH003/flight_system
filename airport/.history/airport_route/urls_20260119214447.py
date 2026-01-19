from .models import Route
from django.urls import path
urlpatterns = [
    path('', views.route_operations, name='route_operations'),
]
