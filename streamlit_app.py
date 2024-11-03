import streamlit as st
import leafmap.foliumap as lm
from ipyleaflet import Map, Marker, Polyline

# Create a Leafmap map instance
m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Define the start and end locations
start = (6.064593, 125.124938)  # Latitude, Longitude
end = (6.064732, 125.127561)

# Create a polyline
route = Polyline(locations=[start, end], color="blue", weight=5)

# Add the polyline to the map
m.add_layer(route)

# Render the map in Streamlit
m.to_streamlit(height=500)
