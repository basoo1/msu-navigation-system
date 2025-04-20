import streamlit as st
import folium as fm
import osmnx as ox
import json
import utility
from folium.plugins import LocateControl as lc
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation

# stremalit setup
st.set_page_config(layout="wide")

def addRoute(m, coords):
    def getRoute(graphType, color, opacity=1.0):

        graph = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type=graphType, simplify=False)

        originNode = ox.distance.nearest_nodes(graph, X=coords[0][1], Y=coords[0][0])
        destNode = ox.distance.nearest_nodes(graph, X=coords[1][1], Y=coords[1][0])

        route = ox.routing.shortest_path(graph, originNode, destNode, weight='length')
        routeCoords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

        fm.PolyLine(locations=routeCoords, color=color, weight=5, opacity=opacity).add_to(m)
        
    getRoute(graphType='walk', color='maroon', opacity=0.5)
    getRoute(graphType='drive_service', color='maroon')

move_search_bar_up = """
    <style>
    div[data-baseweb="input"] {
        margin-top: -4.5em;
    }
    </style>
    """
st.markdown(move_search_bar_up, unsafe_allow_html=True)

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
removerandomelement = """
         <style>
         .stElementContainer.st-key-getLocation-- {
            display: none;
         }
         </style>
         """

st.markdown(custom_margin, unsafe_allow_html=True)
st.markdown(removerandomelement, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)

# preload map
if 'map' not in st.session_state:
    st.session_state['map'] = utility.createMap(lat=0, lng=0)

x = st.text_input('')
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
      geolocation = st.session_state['local_coords']

#check location
   if geolocation:
      
      local_lat = geolocation['coords']['latitude'] 
      local_lng = geolocation['coords']['longitude']

      coords = [(local_lat, local_lng), (location_coords)]

      #main 
      st.session_state["map"] = utility.createMap(lat=local_lat, lng=local_lng)
      addRoute(st.session_state["map"], coords)

      fm.Marker(location=(local_lat, local_lng), icon=fm.Icon(color="blue")).add_to(st.session_state['map'])
      fm.Marker(location=(location_coords), icon=fm.Icon(color="red")).add_to(st.session_state['map'])

st_folium(st.session_state["map"], use_container_width=True, height=500, returned_objects=[])
