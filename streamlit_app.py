import streamlit as st
import leafmap.foliumap as lm
import folium

m = lm.Map(center = [6.064593, 125.124938], zoom = 15)    

start = (6.064593, 125.124938)
end = (6.066119, 125.127561)

route = folium.PolyLine(locations=[start, end], color="blue", weight=5)

m.add_layer(route)

m.to_streamlit(height=500)