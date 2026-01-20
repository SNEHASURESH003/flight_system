from .models import Route

#Example Tree:
# A → B (left, duration=2)
# A → C (right, duration=1)
# B → D (left, duration=3)
# D → F (left, duration=1)
# C → E (right, duration=4)


#nth_left_or_right_node(route=A→B, n=2, direction='left')
#Step 1: current_airport = A → next left route A→B → current_airport = B
#Step 2: current_airport = B → next left route B→D → current_airport = D
#   Return: 'D'


def nth_left_or_right_node(route, n, direction):
    if direction not in ['left', 'right']:
        raise ValueError("Direction must be 'left' or 'right'")
    current_airport = route.airport_code_from
    for step in range(1, n + 1):
        next_route = Route.objects.filter(airport_code_from=current_airport, position=direction ).order_by('id').first()   
        if not next_route:
            return None  
        current_airport = next_route.airport_code_to
    return current_airport.code



#longest_node_on_duration(route=A→B, direction='left')
   #Step 1: current_airport=A → left routes from A: A→B (duration 2) → max_route=A→B → move to B
   #Step 2: current_airport=B → left routes from B: B→D (duration 3) → max_route=B→D → move to D
   #Step 3: current_airport=D → left routes from D: D→F (duration 1) → max_route remains B→D → move to F
   #Step 4: current_airport=F → no left routes → stop
   #Return: 'D'

def longest_node_on_duration(route, direction):
    
    if direction not in ['left', 'right']:
        raise ValueError("Direction must be 'left' or 'right'")
    current_airport = route.airport_code_from
    max_route = None

    while True:
        next_route = Route.objects.filter(airport_code_from=current_airport, position=direction).order_by('-duration').first()  

        if not next_route:
            break
        if not max_route or next_route.duration > max_route.duration:
            max_route = next_route
        current_airport = next_route.airport_code_to
    return max_route.airport_code_to.code if max_route else None




#shortest_node_between_routes(Route1, Route2)
Step 1: Compare durations: 2 <= 5 ✅
Step 2: Return Route1's destination airport code: 'B'
Output: 'B'
def shortest_node_between_routes(route1, route2):
   
    if route1.duration <= route2.duration:
        return route1.airport_code_to.code
    return route2.airport_code_to.code
