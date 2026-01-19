from .models import Route
from django.urls import path
from . import 
urlpatterns = [
   path('airports/add/', add_airport, name='add_airport'),
    path('routes/add/', add_route, name='add_route'),

    path('routes/find-nth/', find_nth_node, name='find_nth'),
    path('routes/longest/<int:route_id>/', find_longest_node, name='longest_node'),
    path('routes/shortest/', find_shortest_between, name='shortest_between'),
]
