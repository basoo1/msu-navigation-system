import streamlit as st
import leafmap.foliumap as lm
import folium
import osmnx as ox

# Enable caching and logging
ox.config(use_cache=True, log_console=True)

# Define the location (General Santos, Philippines)
G = ox.graph_from_place('General Santos, Philippines', network_type='drive')

# Sample route using specific nodes (replace with valid node IDs or use nearest nodes)
# You may need to specify your own valid node IDs or use nearest nodes as shown below
route1 = ox.shortest_path(G, 20461931, 75901933, weight=None)  # Replace with valid node IDs

# Use nearest nodes for origin and destination coordinates
orig = ox.get_nearest_node(G, (6.064593, 125.124938))  # Replace with your origin coordinates
dest = ox.get_nearest_node(G, (6.068402, 125.128223))  # Replace with your destination coordinates

# Calculate the route based on travel time (if data is available)
route2 = ox.shortest_path(G, orig, dest, weight='travel_time')

# Plot the first route (route1)
route_map = ox.plot_route_folium(G, route1, route_color='#ff0000', opacity=0.5)

# Plot the second route (route2) on the same map
route_map = ox.plot_route_folium(G, route2, route_map=route_map, route_color='#0000ff', opacity=0.5)

# Save the map to an HTML file
route_map.save('route.html')
