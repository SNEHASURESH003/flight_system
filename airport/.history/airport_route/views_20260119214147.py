from django.shortcuts import render
from .forms import RouteForm
from .models import Route
from .utils import nth_left_or_right_node, longest_node_on_duration, shortest_node_between_routes
from django.http import HttpResponse
def route_operations(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save()

            # Example operations
            nth_left = nth_left_or_right_node(route, 2, 'left')
            nth_right = nth_left_or_right_node(route, 2, 'right')
            longest_left = longest_node_on_duration(route, 'left')
            longest_right = longest_node_on_duration(route, 'right')

            response = f"""
            Nth Left Node: {nth_left}<br>
            Nth Right Node: {nth_right}<br>
            Longest Left Node: {longest_left}<br>
            Longest Right Node: {longest_right}<br>
            """
            return HttpResponse(response)
    else:
        form = RouteForm()
    return render(request, 'templates/route_form.html', {'form': form})

def home(request):
    return HttpResponse("Welcome to the Airport Route Management System")
from django.shortcuts import render
from .forms import RouteForm
from .models import Route
from .utils import nth_left_or_right_node, longest_node_on_duration, shortest_node_between_routes

