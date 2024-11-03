import streamlit as st
import leafmap.foliumap as lm
import folium
import openrouteservice

# Initialize the OpenRouteService client
ORS_API_KEY = '5b3ce3597851110001cf624837d88bbeea824684aebf5b99dd620f83'  # Replace with your OpenRouteService API key
client = openrouteservice.Client(key='5b3ce3597851110001cf624837d88bbeea824684aebf5b99dd620f83')

# Create the map centered at MSU Gensan
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define start and end points
start = (6.064593, 125.124938)  # Starting coordinates
end = (6.066119, 125.127561)     # Ending coordinates

# Request the route from ORS
route_response = client.directions(
    profile='driving-car',  # Change this to 'cycling-regular', 'foot-walking', etc., as needed
    format='geojson',
    start=start,
    end=end
)

# Extract coordinates from the route response
route_coords = [(point[1], point[0]) for point in route_response['features'][0]['geometry']['coordinates']]

# Create a PolyLine for the route
route = folium.PolyLine(locations=route_coords, color="blue", weight=5)

# Add the route to the map
m.add_layer(route)

# Add markers for start and end points
folium.Marker(start, tooltip='Start').add_to(m)
folium.Marker(end, tooltip='End').add_to(m)

# Display the map in Streamlit
m.to_streamlit(height=500)
