from django.shortcuts import render
from .forms import RouteForm, AirportForm
from .models import Airport, Route
from .utils import nth_left_or_right_node, longest_node_on_duration, shortest_node_between_routes
from django.http import HttpResponse
from django.core.exceptions import ValidationError

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
    return render(request, 'route_form.html', {'form': form})



def add_airport(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Airport added successfully.")
    else:
        form = AirportForm()
    return render(request, 'add_airport.html', {'form': form})

def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Route added successfully.")
    else:
        form = RouteForm()
    return render(request, 'route_form.html', {'form': form})


def find_nth_node(request):
    if request.method == 'POST':
        route_id = request.POST.get('route_id')
        n = int(request.POST.get('n'))
        direction = request.POST.get('direction')

        route = Route.objects.get(id=route_id)
        result = nth_left_or_right_node(route, n, direction)

        return HttpResponse(f"Nth {direction} Node: {result}")
    
    return render(request, 'find_nth_node.html')



