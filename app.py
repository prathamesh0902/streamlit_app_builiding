import streamlit as st
from tile_component import tile
from utils.js_utils import copy_to_clipboard

# --- Page setup ---
st.set_page_config(page_title="Copy Tile App", layout="wide")
st.markdown("<link rel='stylesheet' href='main.css'>", unsafe_allow_html=True)

st.title("🧩 Copy Tile App")

# --- Example tile data ---
tiles = [
    {"title": "Hello", "content": "Hello, World!"},
    {"title": "Python", "content": "print('Hello, Python!')"},
    {"title": "Streamlit", "content": "st.write('Hello from Streamlit!')"}
]

cols = st.columns(3)

for i, t in enumerate(tiles):
    with cols[i]:
        tile(t["title"], t["content"])

# Load JS for clipboard functionality
copy_to_clipboard()
