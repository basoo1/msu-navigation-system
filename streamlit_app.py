import streamlit as st
import leafmap.foliumap as lm
import folium
import requests

# Create a map centered at the specified coordinates
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define start and end coordinates
start = (6.064593, 125.124938)
end = (6.066119, 125.127561)

# Fetch route from OSRM
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full"
response = requests.get(osrm_url)
data = response.json()

if "routes" in data and len(data["routes"]) > 0:
    # Extract the route coordinates
    route = data["routes"][0]["geometry"]["coordinates"]
    # Create a PolyLine for the route
    route_line = folium.PolyLine(locations=[(coord[1], coord[0]) for coord in route], color="blue", weight=5)
    m.add_layer(route_line)
else:
    st.error("No route found.")

# Show the map in Streamlit
m.to_streamlit(height=500)
