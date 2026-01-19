from .models import Route
from .models import Route
from .models import Route

def nth_left_or_right_node(route, n, direction):
    current_route = route

    for _ in range(n):
        next_route = Route.objects.filter(
            airport_code_from=current_route.airport_code_to,
            position=direction
        ).first()

        if not next_route:
            return None

        current_route = next_route

    return current_route.airport_code_to.code



from .models import Route

def longest_node_on_duration(route, direction):
    """
    Returns the airport code of the node with the longest duration in a direction.
    """
    if direction not in ['left', 'right']:
        raise ValueError("Direction must be 'left' or 'right'")

    current_airport = route.airport_code_from
    max_route = None

    while True:
        next_route = Route.objects.filter(
            airport_code_from=current_airport,
            position=direction
        ).first()

        if not next_route:
            break

        if not max_route or next_route.duration > max_route.duration:
            max_route = next_route

        current_airport = next_route.airport_code_to

    return max_route.airport_code_to.code if max_route else None


def shortest_node_between_routes(route1, route2):
    """
    Returns the airport code with the shortest duration between two routes.
    """
    if route1.duration <= route2.duration:
        return route1.airport_code_to.code
    return route2.airport_code_to.code
