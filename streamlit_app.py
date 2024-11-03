import streamlit as st
import leafmap.foliumap as lm
import folium
import openrouteservice as ors

client = ors.Client(key='5b3ce3597851110001cf624837d88bbeea824684aebf5b99dd620f83')

m = lm.Map(center = [6.064593, 125.124938], zoom = 15)    

coords = [((6.064593, 125.124938), (6.064732, 125.127561))]

route = client.directions(coordinates = coords, profile = 'driving car', format = 'geojson')

folium.Polyline(locations=[list(cord) for coord in route['features'][0]['geometry']['coordinates']], color='blue').add_to(m)

m.to_streamlit(height=500)