import streamlit as st
import leafmap.foliumap as lm
import folium
import osmnx as ox
import networkx as nx

m = lm.Map(center=[6.064593, 125.124938], zoom=15)

coords = [(125.124938, 6.064593), (125.128223, 6.068402)]

G = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type='all')

orig_node = ox.distance.nearest_nodes(G, X=coords[0][0], Y=coords[0][1])
dest_node = ox.distance.nearest_nodes(G, X=coords[1][0], Y=coords[1][1])

route = nx.shortest_path(G, orig_node, dest_node, weight='length')

route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

folium.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

# Display the map
m.to_streamlit(height=500)
