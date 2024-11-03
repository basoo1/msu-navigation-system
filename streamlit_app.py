import streamlit as st
import leafmap.foliumap as lm
import folium
import requests

# Define your OpenRouteService API key
ORS_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

def get_route(start, end):
    url = f'https://api.openrouteservice.org/v2/directions/driving-car'
    headers = {
        'Authorization': ORS_API_KEY,
        'Content-Type': 'application/json'
    }
    params = {
        'start': [start[1], start[0]],  # [longitude, latitude]
        'end': [end[1], end[0]]
    }
    response = requests.post(url, headers=headers, json=params)
    return response.json()

# Initialize the map
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define start and end points
start = (6.064593, 125.124938)
end = (6.066119, 125.127561)

# Get route data
route_data = get_route(start, end)

# Extract route coordinates from the response
if 'routes' in route_data:
    route_coords = route_data['routes'][0]['geometry']['coordinates']
    route_coords = [(lat, lon) for lon, lat in route_coords]  # Convert to (lat, lon)

    # Create a PolyLine for the route
    route = folium.PolyLine(locations=route_coords, color="blue", weight=5)
    m.add_layer(route)

# Add markers for start and end points
folium.Marker(location=start, popup='Start', icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=end, popup='End', icon=folium.Icon(color='red')).add_to(m)

# Render the map in Streamlit
m.to_streamlit(height=500)
