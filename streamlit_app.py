import streamlit as st
import leafmap.foliumap as lm

m =  lm.Map

m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
m.add_routing_control(start=(6.1164, 125.1716), end=(6.1184, 125.1736))
