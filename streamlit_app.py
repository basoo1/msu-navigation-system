import streamlit as st
import leafmap.foliumap as lm
import folium

# Create a map centered on MSU Gensan
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define start and end coordinates
start = (6.064593, 125.124938)
end = (6.066119, 125.127561)

# Create a routing layer using Leaflet Routing Machine
routing_layer = folium.LayerControl()
folium.Marker(location=start, popup="Start", icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=end, popup="End", icon=folium.Icon(color='red')).add_to(m)

# Add routing between start and end points
folium.PolyLine(locations=[start, end], color="blue", weight=5, opacity=0.7).add_to(m)

# Initialize routing control
folium.map.LayerControl().add_to(m)

# Convert the map to Streamlit component
m.to_streamlit(height=500)
