import osmnx as ox

# Enable caching and logging
ox.config(use_cache=True, log_console=True)

# Define the location (General Santos, Philippines)
G = ox.graph_from_place('General Santos, Philippines', network_type='drive')

# Use nearest nodes for origin and destination coordinates (General Santos example)
orig = ox.get_nearest_node(G, (6.064593, 125.124938))  # Origin coordinates (replace as needed)
dest = ox.get_nearest_node(G, (6.068402, 125.128223))  # Destination coordinates (replace as needed)

# Calculate the route based on travel time (if data is available)
route2 = ox.shortest_path(G, orig, dest, weight='travel_time')

# Plot the second route (route2) on the map
route_map = ox.plot_route_folium(G, route2, route_color='#0000ff', opacity=0.5)

# Save the map to an HTML file
route_map.save('route.html')
