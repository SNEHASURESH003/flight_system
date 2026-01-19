from .models import Route
from django.urls import path
from .views import add_airport, add_route, dashboard, find_nth_node, find_longest_node, find_shortest_between
from airport_route import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('airports/add/', add_airport, name='add_airport'),
    path('routes/add/', add_route, name='add_route'),
    path('routes/', views.list_routes, name='list_routes'),
    path('routes/edit/<int:route_id>/', views.edit_route, name='edit_route'),
    path('routes/delete/<int:route_id>/', views.delete_route, name='delete_route'),
    path('airports/', views.list_airports, name='list_airports'),
    path('airports/edit/<int:airport_id>/', views.edit_airport, name='edit_airport'),
    path('airports/delete/<int:airport_id>/', views.delete_airport, name='delete_airport'),

    path('routes/find-nth/', find_nth_node, name='find_nth'),
     path('routes/longest-node/<int:route_id>/', find_longest_node, name='longest_node'),
    path('routes/shortest/', find_shortest_between, name='shortest_between'),
     path('/dashboad', dashboard, name='dashboard'),
      path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
