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


from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, get_object_or_404

def find_nth_node(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            route_id = request.POST.get('route_id')
            n = int(request.POST.get('n'))
            direction = request.POST.get('direction')

            route = get_object_or_404(Route, id=route_id)

            if n <= 0:
                error = "N must be greater than zero."
            else:
                result = nth_left_or_right_node(route, n, direction)

                if result is None:
                    error = f"No {n}th node exists in the {direction} direction from this route."

        except ValueError:
            error = "Invalid input. Please enter valid numbers."
        except Exception as e:
            error = str(e)

    return render(request, 'find_nth_node.html', {
        'result': result,
        'error': error
    })




from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

def find_longest_node(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return render(request, 'error.html', {
            'message': 'Route not found. Please enter a valid Route ID.'
        })

    longest_left = longest_node_on_duration(route, 'left')
    longest_right = longest_node_on_duration(route, 'right')

    return render(request, 'longest_node.html', {
        'route': route,
        'longest_left': longest_left,
        'longest_right': longest_right,
    })


from django.shortcuts import render, get_object_or_404

def find_shortest_between(request):
    result = None
    error = None

    if request.method == 'POST':
        route1_id = request.POST.get('route1_id')
        route2_id = request.POST.get('route2_id')

        try:
            route1 = get_object_or_404(Route, id=route1_id)
            route2 = get_object_or_404(Route, id=route2_id)

            result = shortest_node_between_routes(route1, route2)

        except Exception as e:
            error = str(e)

    return render(request, 'shortest_between.html', {
        'result': result,
        'error': error
    })




def dashboard(request):
    return render(request, 'dashboard.html')



