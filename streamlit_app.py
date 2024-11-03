import streamlit as st
import leafmap.foliumap as lm
import folium
import requests
from ipyleaflet import Polyline

# Initialize the map
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define start and end points
start = (6.064593, 125.124938)
end = (6.066119, 125.127454)

# Use OSRM to get the route
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full"
response = requests.get(osrm_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract the route geometry
    route_geo = data['routes'][0]['geometry']
    
    # Decode the polyline to get the route coordinates
    route_coords = polyline.decode(route_geo)

    # Create a polyline for the route
    route_polyline = folium.PolyLine(locations=route_coords, color="blue", weight=5)

    # Add the route to the map
    m.add_layer(route_polyline)

    # Add markers for start and end points
    folium.Marker(location=start, popup='Start', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end, popup='End', icon=folium.Icon(color='red')).add_to(m)
else:
    st.error("Failed to retrieve route data.")

# Render the map in Streamlit
m.to_streamlit(height=500)
