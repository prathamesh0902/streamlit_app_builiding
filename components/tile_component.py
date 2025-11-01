# streamlit_app/components/tile_component.py
import streamlit as st
from streamlit.components.v1 import html

def copy_to_clipboard(text_to_copy):
    """Injects JavaScript to copy text to the clipboard."""
    # Escape quotes for JS string literal
    escaped_text = text_to_copy.replace("'", "\\'") 
    js_code = f"""
    <script>
    navigator.clipboard.writeText('{escaped_text}')
      .then(() => {{
        // Can add a small notification here if desired
      }})
      .catch(err => {{
        console.error('Failed to copy text: ', err);
      }});
    </script>
    """
    html(js_code)

def render_tile(tile_data):
    """
    Renders a single clickable tile that triggers a copy action.
    Uses a form submission to capture the click event in Streamlit's backend.
    """
    tile_id = tile_data['id']
    with st.form(key=f"form_{tile_id}"):
        st.markdown(
            f"""
            <div class="tile" onclick="document.forms['form_{tile_id}'].submit()">
                <div class="tile-text">{tile_data['title']}</div>
                <div class="tile-description">{tile_data['description']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        # A hidden submit button triggered by the JS onclick above
        st.form_submit_button(label="Submit", style="display: none;")
    
    # Check if this specific form was submitted
    if st.session_state.get(f"form_{tile_id}"):
        copy_to_clipboard(tile_data['text_to_copy'])
        st.success(f"Copied text from {tile_data['title']} to clipboard!")
        # Reset the state to prevent continuous triggers
        st.session_state[f"form_{tile_id}"] = False

