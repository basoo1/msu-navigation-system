import streamlit as st
import folium as fm
import osmnx as ox
from folium.plugins import LocateControl as lc
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation
import json
import utility

# Streamlit Setup
st.set_page_config(layout="wide")

hide_st_style = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
custom_margin = """
         <style>
         .block-container 
         {padding-top: 0rem;
         padding-bottom: 0rem;
         padding-left: 0.5rem;
         padding-right: 0.5rem;}
         .element-container 
         </style>
         """
removerandomelement = """
         <style>
         .stElementContainer.st-key-getLocation-- {
            display: none;
         }
         </style>
         """

st.markdown(custom_margin, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(removerandomelement, unsafe_allow_html=True)

if 'map' not in st.session_state:
    st.session_state['map'] = utility.createMap(lat=0, lng=0)

x = st.text_input('Enter Location')

m = utility.createMap(lat=0, lng=0)

local_coords = get_geolocation()

if x:
   with open("locations.json", "r") as file:
      locations = json.load(file)

   result = utility.findMatch(x, locations)

   x = st.empty

   location_details = locations[result]
   location_coords = location_details["coordinates"]

   if local_coords:
      
      local_lat = local_coords['coords']['latitude'] 
      local_lng = local_coords['coords']['longitude']

      coords = [(local_lat, local_lng), (location_coords)]

      st.session_state["map"] = utility.createMap(lat=local_lat, lng=local_lng)
      utility.addRoute(st.session_state["map"], coords)
      fm.Marker(location=(local_lat, local_lng), icon=fm.Icon(color="blue")).add_to(st.session_state['map'])
      fm.Marker(location=(location_coords), icon=fm.Icon(color="red")).add_to(st.session_state['map'])
   else:
      st.error('Unable to obtain device location')

st_folium(st.session_state["map"], use_container_width=True, height=500)
