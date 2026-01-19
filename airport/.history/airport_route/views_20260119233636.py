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


<!DOCTYPE html>
<html lang="en">
<head>
    <title>Find Nth Node</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #020617);
            color: #e5e7eb;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 420px;
            margin: 100px auto;
            background: rgba(30, 41, 59, 0.9);
            padding: 40px;
            border-radius: 18px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        }

        h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #f8fafc;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-size: 14px;
            color: #cbd5f5;
        }

        input, select {
            width: 100%;
            padding: 10px;
            margin-bottom: 18px;
            border-radius: 8px;
            border: none;
            outline: none;
            background-color: #020617;
            color: #f8fafc;
        }

        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #f59e0b, #b45309);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }

        .result-box {
            margin-top: 25px;
            padding: 15px;
            background: #020617;
            border-radius: 10px;
            text-align: center;
            color: #facc15;
            font-weight: bold;
        }

        .error-box {
            margin-top: 20px;
            padding: 12px;
            background: #7f1d1d;
            color: white;
            border-radius: 8px;
            text-align: center;
        }

        .link {
            display: block;
            margin-top: 18px;
            text-align: center;
            color: #60a5fa;
            text-decoration: none;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>🔍 Find Nth Node</h2>

    <form method="post">
        {% csrf_token %}
        <label>Route ID</label>
        <input type="number" name="route_id" required>

        <label>N (Position)</label>
        <input type="number" name="n" required>

        <label>Direction</label>
        <select name="direction">
            <option value="left">Left</option>
            <option value="right">Right</option>
        </select>

        <button type="submit">Search</button>
    </form>

    {% if result %}
        <div class="result-box">
            Result: {{ result }}
        </div>
    {% endif %}

    {% if error %}
        <div class="error-box">
            {{ error }}
        </div>
    {% endif %}

    <a href="{% url 'dashboard' %}" class="link">⬅ Back to Dashboard</a>
</div>

</body>
</html>



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



