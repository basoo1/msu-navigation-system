import folium as fm
import osmnx as ox

def findMatch(user_input, locations):
    for location, details in locations.items():
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

#optimize this
def addRoute(m, coords):
    def getRoute(graphType, color, opacity=1.0):

        graph = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type=graphType, simplify=False)

        originNode = ox.distance.nearest_nodes(graph, X=coords[0][1], Y=coords[0][0])
        destNode = ox.distance.nearest_nodes(graph, X=coords[1][1], Y=coords[1][0])

        route = ox.routing.shortest_path(graph, originNode, destNode, weight='length')
        routeCoords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

        fm.PolyLine(locations=routeCoords, color=color, weight=5, opacity=opacity).add_to(m)

    getRoute(graphType='walk', color='maroon', opacity=0.5)
    getRoute(graphType='drive_service', color='yellow')
