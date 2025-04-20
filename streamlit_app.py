import streamlit as st
import folium as fm
import osmnx as ox
import json
import utility
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation

# streamlit setup
st.set_page_config(layout="wide")

move_search_bar_up = """
   <style>
   .st-emotion-cache-ocqkz7 {
   margin-top: -4.5em;
   }
   <style>
"""

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
   padding-bottom: 0em;
   padding-left: .5rem;
   padding-right: .5rem;}
   .element-container 
   </style>
   """
remove_getLocation = """
   <style>
   .stElementContainer.st-key-getLocation-- {
      display: none;
   }
   </style>
   """

st.markdown(move_search_bar_up, unsafe_allow_html=True)
st.markdown(custom_margin, unsafe_allow_html=True)
st.markdown(remove_getLocation, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)

with open("locations.json", "r") as file:
   locations = json.load(file)   

#create search options table
search_options = []
search_map = {}

#add main location
for location, details in locations.items():
   search_options.append(location)
   search_map[location] = {"location": location, "office": None}

#add options for offices
   for office in details["offices"]:
      display_name = f"{location} ({office})"
      search_options.append(display_name)
      search_map[display_name] = {"location": location, "office": office}

#preload map
if 'map' not in st.session_state:
   st.session_state['map'] = utility.createMap(lat=0, lng=0)


col1, col2 = st.columns([5, 1])

#select box in first column
search_options.sort()
with col1:
   selected_option = st.selectbox('', search_options)

#rerun button in second column
with col2:
   update_button = st.button("Update Location")

#create map
m = utility.createMap(lat=0, lng=0)

if selected_option:
   location_info = search_map.get(selected_option)
   
   if location_info:
      result = location_info["location"]
        
      location_details = locations[result]
      location_coords = location_details["coordinates"]

      if 'local_coords' not in st.session_state:
         geolocation = get_geolocation()
         if geolocation:
               st.session_state['local_coords'] = geolocation
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

         fm.Marker(location=(local_lat, local_lng), 
                  icon=fm.Icon(color="blue")
                  ).add_to(st.session_state['map'])
            
         fm.Marker(location=(location_coords), 
                   icon=fm.Icon(color="red")
                   ).add_to(st.session_state['map'])

st_folium(st.session_state["map"], use_container_width=True, height=500, returned_objects=[])
