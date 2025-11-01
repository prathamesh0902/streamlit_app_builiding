# streamlit_app/app.py
import streamlit as st
from components.tile_component import render_tile

st.set_page_config(page_title="Clickable Tiles App", layout="wide")

st.title("Clickable Tiles with Copy Functionality")

# Load and inject the custom CSS
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data for the four tiles
tile_data_list = [
    {"id": "tile1", "title": "Tile 1", "description": "Click to copy prompt A", "text_to_copy": "This is the text for prompt A."},
    {"id": "tile2", "title": "Tile 2", "description": "Click to copy prompt B", "text_to_copy": "This is the text for prompt B."},
    {"id": "tile3", "title": "Tile 3", "description": "Click to copy prompt C", "text_to_copy": "This is the text for prompt C."},
    {"id": "tile4", "title": "Tile 4", "description": "Click to copy prompt D", "text_to_copy": "This is the text for prompt D."}
]

# Use a container with the CSS class for layout
st.markdown('<div class="tile-container">', unsafe_allow_html=True)

# Render each tile using the component function
cols = st.columns(len(tile_data_list))
for i, tile_data in enumerate(tile_data_list):
    with cols[i]:
        render_tile(tile_data)

st.markdown('</div>', unsafe_allow_html=True)
