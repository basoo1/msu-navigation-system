import streamlit as st
import leafmap.foliumap as lm
import folium

m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

start = (6.064593, 125.124938)
end = (6.064732, 125.127561)

route = folium.PolyLine(locations=[start, end], color="blue", weight=5)

route.add_to(m)

m.to_streamlit(height=500)