import streamlit as st
import leafmap.foliumap as lm
import folium

# Create a Leafmap map instance
m = lm.Map(minimap_control=True)
m.add_basemap("OpenStreetMap")

# Define the start and end locations
start = (6.064593, 125.124938)  # Latitude, Longitude for the start point
end = (6.064732, 125.127561)    # Latitude, Longitude for the end point

# Create markers for start and end points
folium.Marker(location=start, popup='Start Point').add_to(m)
folium.Marker(location=end, popup='End Point').add_to(m)

# Add Leaflet Routing Machine script using OSRM
routing_script = f"""
<script>
var control = L.Routing.control({{
    waypoints: [
        L.latLng({start[0]}, {start[1]}),
        L.latLng({end[0]}, {end[1]})
    ],
    routeWhileDragging: true,
    geocoder: L.Control.Geocoder.nominatim(),
    createMarker: function() {{ return null; }},  // Prevent markers from being created
    router: L.Routing.osrmv1({{ serviceUrl: 'https://router.project-osrm.org/' }})  // OSRM routing service
}}).addTo(map);
</script>
"""

# Add the routing script to the map
m.add_child(folium.Element(routing_script))

# Render the map in Streamlit
st.title("Leaflet Routing Machine with OSRM Example")
m.to_streamlit(height=500)
