import folium as fm
import osmnx as ox
import base64
import streamlit as st

def findMatch(user_input, locations):
    #check exact math in locations
    for location, details in locations.items():
        if location.lower() == user_input.lower():
            return location
    
    #check mathing aliases
    for location, details in locations.items():
        for alias in details["aliases"]:
            if alias.lower() == user_input.lower():
                return location
    
    #check matching ofiecs
    for location, details in locations.items():
        for office in details["offices"]:
            if office.lower() == user_input.lower():
                return location
    
    #if no match, check prefix 
    for location, details in locations.items():
        if location.lower().startswith(user_input.lower()):
            return location
        
        for alias in details["aliases"]:
            if alias.lower().startswith(user_input.lower()):
                return location
        
        for office in details["offices"]:
            if office.lower().startswith(user_input.lower()):
                return location
    
    return "No match found."

def createMap(lat, lng):
    minLat, maxLat = 6.07406, 6.06009
    minLon, maxLon = 125.13257, 125.12135

    m = fm.Map(location=[lat, lng], 
               zoom_start=16,
               max_bounds=True,
               min_lat=minLat,
               max_lat=maxLat,
               min_lon=minLon,
               max_lon=maxLon,
               min_zoom=16,
               )
    return m

def addRoute(m, coords):
    def getRoute(graphType, color, opacity=1.0):

        graph = ox.graph_from_point(center_point=coords[0], dist=1000, network_type=graphType, simplify=False)

        originNode = ox.distance.nearest_nodes(graph, X=coords[0][1], Y=coords[0][0])
        destNode = ox.distance.nearest_nodes(graph, X=coords[1][1], Y=coords[1][0])

        route = ox.routing.shortest_path(graph, originNode, destNode, weight='length')
        routeCoords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

        routeFG = fm.FeatureGroup(name='Polylines')

        fm.PolyLine(locations=routeCoords, color=color, weight=5, opacity=opacity).add_to(routeFG)

        routeFG.add_to(m)

    getRoute(graphType='walk', color='maroon', opacity=0.5)
    getRoute(graphType='drive_service', color='maroon')


# Set background
def get_img_b64(file):
   with open(file, "rb") as f:
      data = f.read()
   return base64.b64encode(data).decode()

def set_bg(image_path):
    base64_image = get_img_b64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{base64_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_sidebar_button(image_path):
    base64_image = get_img_b64(image_path)
    st.markdown(
    f"""
    <style>
    [data-testid="stSidebarCollapsedControl"] {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: transparent;
    }}
    .stBaseButton-headerNoPadding
    </style>
""", unsafe_allow_html=True)
