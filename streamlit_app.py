import streamlit as st
import leafmap

# Title of the app
st.title("Interactive Leafmap with Streamlit")

# Create a Leafmap instance
m = leafmap.Map()

# Add a basemap
m.add_basemap("OpenStreetMap")

# Add a marker for a specific location (e.g., MSU Gensan)
m.add_marker(location=[6.1079, 125.1456], popup="MSU Gensan")

# Display the map in the Streamlit app
m.to_streamlit(height=600)

# Optional: Add additional functionalities
st.sidebar.header("Map Controls")
option = st.sidebar.selectbox("Select a feature", ["Marker", "Polygon", "Circle"])

if option == "Polygon":
    coordinates = st.sidebar.text_input("Enter coordinates (lat, lon):", value="6.1079, 125.1456; 6.1080, 125.1460")
    if st.sidebar.button("Add Polygon"):
        coords_list = [list(map(float, coord.split(','))) for coord in coordinates.split(';')]
        m.add_polygon(coords_list, color="blue", fill=True, fill_opacity=0.4)

elif option == "Circle":
    lat = st.sidebar.number_input("Latitude", value=6.1079)
    lon = st.sidebar.number_input("Longitude", value=125.1456)
    radius = st.sidebar.number_input("Radius (meters)", value=100)
    if st.sidebar.button("Add Circle"):
        m.add_circle_marker(location=[lat, lon], radius=radius, color="green", fill=True, fill_opacity=0.4)

# Show the updated map
m.to_streamlit(height=600)
