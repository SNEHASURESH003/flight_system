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

def longest_node_on_duration