import folium as fm
import osmnx as ox

from folium.plugins import MousePosition

def findMatch(user_input, locations):
    for location, details in locations.items():
        # check if the user input matches the prefix of each locations
        for name in [location] + details["aliases"]:
            if name.lower().startswith(user_input.lower()):
                return location
    
    return "No match found."

def createMap():
    minLat, maxLat = 6.07406, 6.06009
    minLon, maxLon = 125.13257, 125.12135

    m = fm.Map(location=[6.064593, 125.124938], 
               zoom_start=16,
               max_bounds=True,
               min_lat=minLat,
               max_lat=maxLat,
               min_lon=minLon,
               max_lon=maxLon,
               min_zoom=16)
    return m

def addRoute(m, coords):
    G = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type='all')

    orig_node = ox.distance.nearest_nodes(G, X=coords[0][1], Y=coords[0][0])
    dest_node = ox.distance.nearest_nodes(G, X=coords[1][1], Y=coords[1][0])

    route = ox.routing.shortest_path(G, orig_node, dest_node, weight='length')
    route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

    fm.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

#using mouse for testing
def getUserLocation(m):
    MousePosition().add_to(m)
