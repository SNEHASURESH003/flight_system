from django.shortcuts import render
from .forms import RouteForm, AirportForm
from .models import Airport, Route
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
def add_routes_between_airports(request):
    if request.method == 'POST':
        from_code = request.POST.get('from_code')
        to_code = request.POST.get('to_code')
        position = request.POST.get('position')
        duration = request.POST.get('duration')
        distance = request.POST.get('distance')

        try:
            airport_from = Airport.objects.get(code=from_code)
            airport_to = Airport.objects.get(code=to_code)

            route = Route(
                airport_code_from=airport_from,
                airport_code_to=airport_to,
                position=position,
                duration=duration,
                distance=distance
            )
            route.full_clean()  # Validate the route
            route.save()
            return HttpResponse("Route added successfully.")
        except Airport.DoesNotExist:
            return HttpResponse("One of the specified airports does not exist.")
        except ValidationError as e:
            return HttpResponse(f"Validation error: {e.messages}")
    return render(request, 'add_route.html')


