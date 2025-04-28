import streamlit as st
import folium as fm
import osmnx as ox
import json
import utility
import streamlit.components.v1 as components
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation

# streamlit setup
st.set_page_config(layout="wide")
markerFG = fm.FeatureGroup(name='Markers')

move_search_bar_up = """
   <style>
   .stSelectbox {
   margin-top: -4.5em;
   }
   <style>
"""

move_sidebar_collapse_button = """
   <style>
   [data-testid="stSidebarCollapsedControl"] {
      margin-top: 19rem;
      margin-left: -1.5rem;
   }
   </style>
"""

move_sidecontrol = """
   <style>
   stBaseButton-headerNoPadding {
   margin-bottom: -4.5em;
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
st.markdown(move_sidebar_collapse_button, unsafe_allow_html=True)

with open("locations.json", "r") as file:
   locations = json.load(file)   

#create search options table
search_options = []
search_map = {}

#add main location
for location, details in locations.items():
   search_options.append(location)
   search_map[location] = {"location": location, "office": None}

#preload map
if 'map' not in st.session_state:
   st.session_state['map'] = utility.createMap(lat=0, lng=0)


selected_option = st.selectbox('Search', search_options)

#create sidebar
sidebar = st.sidebar

if selected_option:
   location_info = search_map.get(selected_option)
   
   if location_info:
      result = location_info["location"]
        
      location_details = locations[result]
      location_coords = location_details["coordinates"]
      
      #display
      sidebar.header(result)
      if location_details["offices"]:
          sidebar.subheader("Offices:")
          for office in location_details["offices"]:
              sidebar.write(f"• {office}")
      else:
          sidebar.write("No offices found in this building.")

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
                  ).add_to(markerFG)
            
         fm.Marker(location=(location_coords), 
                  icon=fm.Icon(color="red"),
                  popup=selected_option
                  ).add_to(markerFG)
         markerFG.add_to(st.session_state['map'])

st_folium(st.session_state["map"], 
          use_container_width=True, 
          feature_group_to_add=markerFG,
          returned_objects=[])
