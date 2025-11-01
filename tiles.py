import streamlit as st
from st_clipboard import copy_to_clipboard
from streamlit_extras.colored_header import colored_header
from streamlit_extras.row import row

st.set_page_config(page_title="Clickable Tiles App", layout="wide")

def create_tile(title, text_to_copy, key):
    """A function to create a clickable 'tile' using a button and copy component."""
    
    # Custom CSS for the tile appearance
    st.markdown(f"""
    <style>
    .tile-container {{
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        cursor: pointer;
    }}
    .tile-container:hover {{
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }}
    .tile-title {{
        font-size: 18px;
        font-weight: bold;
    }}
    .tile-text {{
        font-size: 14px;
        color: #555;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Use a button to capture the click action and use the copy component
    if st.button(label=f"📋 Copy: {title}", key=f"btn_{key}"):
        copy_to_clipboard(text_to_copy)
        st.success(f"Copied '{title}' text to clipboard!")

    # Display the tile content using markdown for styling (not clickable itself, but the button handles the action)
    st.markdown(f"""
    <div class="tile-container">
        <div class="tile-title">{title}</div>
        <div class="tile-text">{text_to_copy}</div>
    </div>
    """, unsafe_allow_html=True)


st.title("Clickable Tiles to Copy Text")

# Create a row for the tiles using streamlit-extras
my_row = row(4, vertical_align="center")

with my_row.col():
    create_tile("Tile 1: Email Address", "user@example.com", "tile1")

with my_row.col():
    create_tile("Tile 2: Command Line", "pip install streamlit", "tile2")

with my_row.col():
    create_tile("Tile 3: API Key", "API_KEY_XYZ_12345", "tile3")

with my_row.col():
    create_tile("Tile 4: Phone Number", "+1-555-123-4567", "tile4")

