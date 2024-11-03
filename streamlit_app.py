import streamlit as st
import leafmap.foliumap as lm
from ipyleaflet import Map, Marker, Polyline

m =  lm.Map

m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

start = (6.064593, 125.124938)  # Latitude, Longitude
end = (6.064732, 125.127561)

route = Polyline(locations=[start, end], color="blue", weight=5)
m.add_layer 
