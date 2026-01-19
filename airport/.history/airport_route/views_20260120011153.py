from django.shortcuts import render, get_object_or_404, redirect
from .forms import RouteForm, AirportForm
from .models import Airport, Route
from .utils import nth_left_or_right_node, longest_node_on_duration, shortest_node_between_routes
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages 

from django.contrib.auth.decorators import login_required, user_passes_test

# Only allow superusers
def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def dashboard(request):
    
    airports = Airport.objects.all()
    routes = Route.objects.all()
    return render(request, 'dashboard.html', {'airports': airports, 'routes': routes})


#Add Airport

@login_required
@user_passes_test(superuser_required)
def add_airport(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Airport added successfully!")  
            
    else:
        form = AirportForm()
    return render(request, 'add_airport.html', {'form': form})

# List Airports 

@login_required
@user_passes_test(superuser_required)
def list_airports(request):
    airports = Airport.objects.all()
    return render(request, 'list_airports.html', {'airports': airports})

# Edit Airport

@login_required
@user_passes_test(superuser_required)
def edit_airport(request, airport_id):
    airport = get_object_or_404(Airport, id=airport_id)
    if request.method == 'POST':
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            messages.success(request, "Airport updated successfully!")
            return redirect('list_airports')
    else:
        form = AirportForm(instance=airport)
    return render(request, 'edit_airport.html', {'form': form, 'airport': airport})

# Delete Airport
def delete_airport(request, airport_id):
    airport = get_object_or_404(Airport, id=airport_id)
    if request.method == 'POST':
        airport.delete()
        messages.success(request, "Airport deleted successfully!")
        return redirect('list_airports')
    return render(request, 'delete_airport.html', {'airport': airport})

#Add airport route
def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Route added successfully!")
            return redirect('list_routes')
    else:
        form = RouteForm()
    return render(request, 'route_form.html', {'form': form, 'title': 'Add Airport Route'})


# List Routes
def list_routes(request):
    routes = Route.objects.all()
    return render(request, 'list_routes.html', {'routes': routes})

# Edit Route
def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            messages.success(request, "Route updated successfully!")
            return redirect('list_routes')
    else:
        form = RouteForm(instance=route)
    return render(request, 'route_form.html', {'form': form, 'title': f'Edit Route {route.id}'})

# Delete Route
def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        route.delete()
        messages.success(request, "Route deleted successfully!")
        return redirect('list_routes')
    return render(request, 'delete_route.html', {'route': route})



#Find Nth node in an airport route
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

    return render(request, 'find_nth_node.html', {  'result': result, 'error': error  })





#Find Longest Node  based on duration
def find_longest_node(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        return render(request, 'error.html', {
            'message': 'Route not found. Please enter a valid Route ID.'})

    longest_left = longest_node_on_duration(route, 'left')
    longest_right = longest_node_on_duration(route, 'right')

    return render(request, 'longest_node.html', {
        'route': route,
        'longest_left': longest_left,
        'longest_right': longest_right,
    })



#Find Shortest Node based on duration between two routes
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






