import streamlit as st
import leafmap.foliumap as lm
import folium
import openrouteservice as ors

client = ors.Client(key='5b3ce3597851110001cf624837d88bbeea824684aebf5b99dd620f83')

m = lm.Map(center=[6.064593, 125.124938], zoom=15)

coords = [(125.124938, 6.064593), (125.128223, 6.068402)]

route = client.directions(
    coordinates=coords, 
    profile='driving-car', 
    format='geojson'
)

route_coords = [(coord[1], coord[0]) for coord in route['features'][0]['geometry']['coordinates']]
folium.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

# Display
m.to_streamlit(height=500)
