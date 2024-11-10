import streamlit as st
import leafmap.foliumap as lm
import folium
import networkx as nx
import osmnx as ox

# Create the map
m = lm.Map(center=[6.064593, 125.124938], zoom=15)

# Define the coordinates for the route (start and end)
coords = [(125.124938, 6.064593), (125.128223, 6.068402)]

# Download the street network for a specific area (e.g., a part of General Santos City)
place_name = "General Santos, Philippines"  # Modify this as needed
graph = ox.graph_from_place(place_name, network_type='all')

# Convert coordinates to nearest nodes on the graph
start_node = ox.distance.nearest_nodes(graph, X=coords[0][0], Y=coords[0][1])
end_node = ox.distance.nearest_nodes(graph, X=coords[1][0], Y=coords[1][1])

# Find the shortest path using Dijkstra's algorithm
shortest_path = nx.shortest_path(graph, source=start_node, target=end_node, weight='length')

# Get coordinates for the route from the graph
route_coords = [(graph.nodes[node]['x'], graph.nodes[node]['y']) for node in shortest_path]

# Add the route to the map
folium.PolyLine(locations=route_coords, color='blue', weight=5).add_to(m)

# Display the map in Streamlit
m.to_streamlit(height=500)
