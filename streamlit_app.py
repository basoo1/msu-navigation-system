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

m
