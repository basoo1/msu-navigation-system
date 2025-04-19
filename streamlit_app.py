import streamlit as st
import folium as fm
import osmnx as ox
from folium.plugins import LocateControl as lc
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation
import json
import utility

# stremalit setup
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    html, body, .block-container {
        height: 100vh;
        margin: 0;
        padding: 0;
    }

    .block-container {
        display: flex;
        flex-direction: column;
    }

    .map-container {
        flex-grow: 1;
    }

    .stTextInput input {
        width: 100%;
        padding: 10px;
        font-size: 1rem;
    }

    #MainMenu, header, footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)
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
         {padding-top: 1.3rem;
         padding-bottom: 1.3em;
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
st.markdown(removerandomelement, unsafe_allow_html=True)

# preload map
if 'map' not in st.session_state:
    st.session_state['map'] = utility.createMap(lat=0, lng=0)

x = st.text_input('Enter Location')
m = utility.createMap(lat=0, lng=0)

#check locatations file
if x:
   with open("locations.json", "r") as file:
      locations = json.load(file)   

   result = utility.findMatch(x, locations)

   location_details = locations[result]
   location_coords = location_details["coordinates"]

   if 'local_coords' not in st.session_state:
      geolocation = get_geolocation()
      if geolocation:
         st.session_state['local_coords'] = geolocation
      else:
         st.error("Please wait while we get your device's location.")
   else:
      geolocation = st.session_state['local_coords']

#check location
   if geolocation:
      
      local_lat = geolocation['coords']['latitude'] 
      local_lng = geolocation['coords']['longitude']

      coords = [(local_lat, local_lng), (location_coords)]

      #main 
      st.session_state["map"] = utility.createMap(lat=local_lat, lng=local_lng)
      utility.addRoute(st.session_state["map"], coords)

      fm.Marker(location=(local_lat, local_lng), icon=fm.Icon(color="blue")).add_to(st.session_state['map'])
      fm.Marker(location=(location_coords), icon=fm.Icon(color="red")).add_to(st.session_state['map'])

st_folium(st.session_state["map"], use_container_width=True, height=600, returned_objects=[])
