def nth_left_or_right(routes, n, direction):
    """
    Get the nth left or right route from a list of routes.

    :param routes: List of Route objects
    :param n: The nth position to retrieve (1-based index)
    :param direction: 'left' or 'right'
    :return: The nth Route object in the specified direction or None if not found
    """
    filtered_routes = [route for route in routes if route.position.lower() == direction.lower()]
    if 0 < n <= len(filtered_routes):
        return filtered_routes[n - 1]
    return None


def 