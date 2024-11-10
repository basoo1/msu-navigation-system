import streamlit as st
import leafmap.foliumap as lm
import folium
import osmnx as ox
import networkx as nx

# Create a map centered on MSU Gensan
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define coordinates
coords = [(125.124938, 6.064593), (125.128223, 6.068402)]

# Download the street network from OpenStreetMap around the coordinates
G = ox.graph_from_place('Mindanao State University General Santos, General Santos, Philippines', network_type='all')

# Convert coordinates to the nearest nodes in the graph
orig_node = ox.distance.nearest_nodes(G, X=coords[0][0], Y=coords[0][1])
dest_node = ox.distance.nearest_nodes(G, X=coords[1][0], Y=coords[1][1])

# Get the route between the nodes
route = nx.shortest_path(G, orig_node, dest_node, weight='length')

# Convert the route to coordinates
route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

# Plot the route on the map
folium.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

# Display the map
m.to_streamlit(height=500)
