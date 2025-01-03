import streamlit as st
import folium as fm
import osmnx as ox
from streamlit_folium import st_folium
from folium.plugins import Fullscreen
from folium.plugins import MousePosition
import json
import utility

#Streamlit Setup
st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
remove_top_margin = """
            <style>
            .block-container 
            {padding-top: 0.5rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;}
            </style>
            """

st.markdown(remove_top_margin, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)
st.container(height=None, border=None, key=None)


x = st.text_input("Enter Location")
with open("locations.json", "r") as file:
    locations = json.load(file)
result = utility.findMatch(x, locations)
location_details = locations[result]
location_coords = location_details["coordinates"]
coords = [(125.124938, 6.064593), (location_coords)]
m =  utility.createMap()
utility.addRoute(m, coords)
Fullscreen().add_to(m)
MousePosition().add_to(m)
st_folium(m, use_container_width=True)
