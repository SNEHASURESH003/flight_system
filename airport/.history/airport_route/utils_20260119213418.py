from .models import Route
def nth_left_or_right_node(route, n, direction):
    """
    Returns the nth left or right node from the given route.
    direction: 'left' or 'right'
    """
    if direction not in ['left', 'right']:
        raise ValueError("Direction must be 'left' or 'right'")

    current_route = route
    count = 0

    while current_route and count < n:
        next_routes = Route.objects.filter(
            airport_code_from=current_route.airport_code_to,
            position=direction
        )
        if not next_routes.exists():
            return None
        current_route = next_routes.first()
        count += 1

    return current_route.airport_code_to if current_route else None

def longest_node_on_duration(route, direction):
    """
    Returns the airport code of the node with the longest duration in the specified direction.
    direction: 'left' or 'right'
    """
    if direction not in ['left', 'right']:
        raise ValueError("Direction must be 'left' or 'right'")

    current_route = route
    max_duration = current_route.duration
    longest_airport = current_route.airport_code_to

    while current_route:
        next_routes = Route.objects.filter(
            airport_code_from=current_route.airport_code_to,
            position=direction
        )
        if not next_routes.exists():
            break
        current_route = next_routes.first()
        if current_route.duration > max_duration:
            max_duration = current_route.duration
            longest_airport = current_route.airport_code_to

    return longest_airport


def shortest_node_between_routes(route1, route2):
    """
    Returns the airport code of the node with the shortest duration between two routes.
    """
    if route1.airport_code_to != route2.airport_code_from:
        raise ValueError("The destination of route1 must be the source of route2")

    if route1.duration < route2.duration:
        return route1.airport_code_to
    else:
        return route2.airport_code_from
    