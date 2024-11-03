import streamlit as st
import leafmap.foliumap as lm

m =  lm.Map

m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)