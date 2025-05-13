import streamlit as st
import folium as fm
import osmnx as ox
import json
import utility
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation

#streamlit setup
st.set_page_config(layout="wide")
markerFG = fm.FeatureGroup(name='Markers')

hide_st_style = """
   <style>
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   header {visibility: hidden;}
   </style>
   """

custom_margin = """
   <style>
   .block-container {
      padding-top: 0rem;
      padding-bottom: 0em;
      padding-left: 0rem;
      padding-right: 0rem;}
   }
   </style>
   """
c_SearchBox = """
   <style>
   [data-testid="stSelectbox"] {
      margin-top: -4.5rem;
      padding-left: .5rem;
      padding-right: .5rem;
      z-index: 999;
   }

   /* downSymbol */
   .st-ck {
      fill: #800000;
   }

   /* Title Size */
   [data-testid="stMarkdownContainer"] {
      font-size: 1.2rem;
   }

   /* Title */
   p, ol, ul, dl {
      margin: 0px 0px 1rem;
      padding: 0px;
      font-size: 1rem;
      font-weight: 800;
      color: #800000
   }
   <style>
"""

c_Map = """
   <style>
   .stElementContainer.st-key-getLocation-- {
      display: none;
   }
   </style>
   """

c_sideBar = """
   <style>
   [data-testid="stSidebarCollapsedControl"] {
      margin-top: 19rem;
      margin-left: -2rem;
   }
   [data-testid="stBaseButton-headerNoPadding"] {
      background-color: rgb(255 255 255);
      color: #800000;
   }
   [data-testid="stSidebar"] {
      background-color: #ffffff
   }

   /*Building Text*/
   .st-emotion-cache-102y9h7 h2 {
    font-size: 1.5rem;
    padding-right: 0rem;
    margin-top: -2.2rem;
   }

   /*Offices Text*/
   .st-emotion-cache-102y9h7 h3 {
      font-size: 1.3rem;
      margin-top: -1.6em;
   }

   .st-emotion-cache-a6qe2i {
    padding: 0rem 1.5rem 6rem;
   }
   <style>
"""

st.markdown(c_SearchBox, unsafe_allow_html=True)
st.markdown(custom_margin, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(c_Map, unsafe_allow_html=True)
st.markdown(c_sideBar, unsafe_allow_html=True)

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

selected_option = st.selectbox('MAPA ISKO', search_options, index=None, placeholder="Search")

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
                  icon=fm.Icon(color="blue"),
                  popup="Your Location"
                  ).add_to(markerFG)

         fm.Marker(location=(location_coords), 
                  icon=fm.Icon(color="red"),
                  popup=selected_option
                  ).add_to(markerFG)
         
         markerFG.add_to(st.session_state['map'])

st_folium(st.session_state["map"], 
   use_container_width=True, 
   height=500,
   feature_group_to_add=markerFG,
   returned_objects=[])

