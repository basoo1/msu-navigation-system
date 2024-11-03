import streamlit as st
import leafmap.foliumap as lm
from ipyleaflet import Map, Marker, Polyline
from ipywidgets import HTML

# Create a new Leafmap instance
m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Define start and end coordinates
start = (6.064593, 125.124938)  # Latitude, Longitude
end = (6.064732, 125.127561)

# Add markers for start and end points
start_marker = Marker(location=start, title="Start")
end_marker = Marker(location=end, title="End")
m.add_marker(start_marker)
m.add_marker(end_marker)

# Create a routing feature
route = Polyline(locations=[start, end], color="blue", weight=5)
m.add_layer(route)

# Display the map in Streamlit
m.to_streamlit(height=500)
