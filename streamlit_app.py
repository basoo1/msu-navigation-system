import streamlit as st
import leafmap.foliumap as lm
import folium

# Create a Leafmap map instance
m = lm.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Define the start and end locations
start = (6.064593, 125.124938)  # Latitude, Longitude
end = (6.064732, 125.127561)

# Create a Marker for the start point
folium.Marker(location=start, popup='Start Point').add_to(m)

# Create a Marker for the end point
folium.Marker(location=end, popup='End Point').add_to(m)

# Draw a straight line (polyline) from start to end
folium.PolyLine(locations=[start, end], color="blue", weight=5).add_to(m)

# Add routing using Leaflet Routing Machine
routing_script = f"""
<script>
var control = L.Routing.control({{
    waypoints: [
        L.latLng({start[0]}, {start[1]}),
        L.latLng({end[0]}, {end[1]})
    ],
    routeWhileDragging: true,
    geocoder: L.Control.Geocoder.nominatim(),
    createMarker: function() {{ return null; }}  // Prevent markers from being created
}}).addTo(map);
</script>
"""

# Add the routing script to the map
m.add_child(folium.Element(routing_script))

# Render the map in Streamlit
m.to_streamlit(height=500)
