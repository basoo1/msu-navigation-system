import streamlit as st
import folium as fm
import osmnx as ox
import streamlit.components.v1 as stc
from streamlit_folium import st_folium
from folium.plugins import Fullscreen
from streamlit_js_eval import get_geolocation
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
removethatfuckingpieceofshitrandomaahhhelement = """
         <style>
         .stElementContainer.st-key-getLocation-- {
           display: none;
         }
         </style>
         """

st.markdown(custom_margin, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(removethatfuckingpieceofshitrandomaahhhelement, unsafe_allow_html=True)

x = st.text_input("Enter Location")

if x:
   with open("locations.json", "r") as file:
      locations = json.load(file)
   result = utility.findMatch(x, locations)
   location_details = locations[result]
   location_coords = location_details["coordinates"]

   local_coords = get_geolocation()

   if local_coords:
      local_lat = local_coords['coords']['latitude'] 
      local_lng = local_coords['coords']['longitude']

      coords = [(local_lat, local_lng), (location_coords)]
    
      #map creation
      m =  utility.createMap(lat=local_lat, lng=local_lng)   
      utility.addRoute(m, coords)
      Fullscreen().add_to(m)
      st_folium(m, use_container_width=True)
