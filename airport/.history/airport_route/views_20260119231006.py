from django.shortcuts import render
from .forms import RouteForm, AirportForm
from .models import Airport, Route
from .utils import nth_left_or_right_node, longest_node_on_duration, shortest_node_between_routes
from django.http import HttpResponse
from django.core.exceptions import ValidationError




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


def find_longest_node(request, route_id):
    route = Route.objects.get(id=route_id)
    longest_left = longest_node_on_duration(route, 'left')
    longest_right = longest_node_on_duration(route, 'right')

    return HttpResponse(
        f"Longest Left Node: {longest_left}<br>"
        f"Longest Right Node: {longest_right}"
    )

def find_shortest_between(request):
    if request.method == 'POST':
        route1_id = request.POST.get('route1_id')
        route2_id = request.POST.get('route2_id')

        route1 = Route.objects.get(id=route1_id)
        route2 = Route.objects.get(id=route2_id)

        result = shortest_node_between_routes(route1, route2)

        return HttpResponse(f"Shortest Node Between Routes: {result}")

    return render(request, 'shortest_between.html')



def dashboard(request):
    return render(request, 'dashboard.html')



