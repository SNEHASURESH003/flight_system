from .models import Route

urlpatterns = [
    path('', views.route_operations, name='route_operations'),
]
