import streamlit as st
import leafmap.foliumap as lm
import folium  # Ensure you have this imported

# Create a Leafmap map instance
m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Define the start and end locations
start = (6.064593, 125.124938)  # Latitude, Longitude
end = (6.064732, 125.127561)

# Create a PolyLine using Folium
route = folium.PolyLine(locations=[start, end], color="blue", weight=5)

# Add the PolyLine to the map
route.add_to(m)  # Use add_to method with the Leafmap instance

# Render the map in Streamlit
m.to_streamlit(height=500)
