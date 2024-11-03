import leafmap
from ipyleaflet import Map, Marker, Polyline
import requests

# Create a map
m = leafmap.Map(center=(14.5875, 120.9758), zoom=14)

# Define start and end points
start = (14.5875, 120.9758)  # Starting point
end = (14.6011, 120.9949)    # Ending point

# Add markers
start_marker = Marker(location=start, draggable=False)
end_marker = Marker(location=end, draggable=False)
m.add_layer(start_marker)
m.add_layer(end_marker)

# Fetch route from OSRM
response = requests.get(f'http://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full')
data = response.json()

# Extract route coordinates
route = data['routes'][0]['geometry']['coordinates']
route_coords = [(point[1], point[0]) for point in route]

# Create a polyline for the route
route_line = Polyline(locations=route_coords, color='blue', weight=5)

# Add the polyline to the map
m.add_layer(route_line)

# Display the map
m
