import streamlit as st
import leafmap.foliumap as lm

# Create the map
m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Define start and end coordinates
start = (6.064593, 125.124938)  # (latitude, longitude)
end = (6.064732, 125.127561)

# Add markers for start and end points
m.add_marker(location=start, popup="Start", icon='blue')
m.add_marker(location=end, popup="End", icon='red')

# Custom JavaScript to add routing
routing_js = """
<script src="https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet-routing-machine/dist/leaflet-routing-machine.css" />

<script>
    var control = L.Routing.control({
        waypoints: [
            L.latLng(6.064593, 125.124938),
            L.latLng(6.064732, 125.127561)
        ],
        routeWhileDragging: true
    }).addTo(map);
</script>
"""

# Display the map in Streamlit
m.to_streamlit(height=500)

# Add the custom JavaScript to the Streamlit app
st.components.v1.html(routing_js, height=0)