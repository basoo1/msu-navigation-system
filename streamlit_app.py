import streamlit as st
import leafmap.foliumap as lm
import folium
import openrouteservice as ors

# Initialize the OpenRouteService client with your API key
client = ors.Client(key='5b3ce3597851110001cf624837d88bbeea824684aebf5b99dd620f83')

# Set up the map centered at MSU Gensan
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define coordinates in (longitude, latitude) order
coords = [(125.124938, 6.064593), (125.127459, 6.066119)]

# Request the route from OpenRouteService
route = client.directions(
    coordinates=coords, 
    profile='driving-car', 
    format='geojson'
)

# Extract the route coordinates and create a PolyLine
route_coords = [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]
folium.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

# Display the map in Streamlit
m.to_streamlit(height=500)
