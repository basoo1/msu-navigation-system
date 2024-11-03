import streamlit as st
import leafmap.foliumap as lm

m =  lm.Map

m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
m.add_routing_control(start=(125.170273,6.109288), end=(125.178931,6.109299))
