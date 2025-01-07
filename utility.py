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
               min_zoom=16)
    return m

def addRoute(m, coords):

    #walk mode
    walk_graph = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type='walk')

    orig_node_walk = ox.distance.nearest_nodes(walk_graph, X=coords[0][1], Y=coords[0][0])
    dest_node_walk = ox.distance.nearest_nodes(walk_graph, X=coords[1][1], Y=coords[1][0])

    walk_route = ox.routing.shortest_path(walk_graph, orig_node_walk, dest_node_walk, weight='length')
    walk_route_coords = [(walk_graph.nodes[node]['y'], walk_graph.nodes[node]['x']) for node in walk_route]


    fm.PolyLine(locations=walk_route_coords, color='blue', weight=5, opacity=0.5).add_to(m)

    #drive mode
    drive_graph = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type='drive_service')

    orig_node_drive = ox.distance.nearest_nodes(drive_graph, X=coords[0][1], Y=coords[0][0])
    dest_node_drive = ox.distance.nearest_nodes(drive_graph, X=coords[1][1], Y=coords[1][0])

    drive_route = ox.routing.shortest_path(drive_graph, orig_node_drive, dest_node_drive, weight='length')
    drive_route_coords = [(drive_graph.nodes[node]['y'], drive_graph.nodes[node]['x']) for node in drive_route]

    fm.PolyLine(locations=drive_route_coords, color='blue', weight=5).add_to(m)

#using mouse for testing
def getUserLocation(m):
    MousePosition().add_to(m)
