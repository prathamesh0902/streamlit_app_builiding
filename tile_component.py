import streamlit as st

def tile(title, content):
    button_id = f"copy-btn-{title.replace(' ', '_')}"
    
    st.markdown(f"""
        <div class="tile" id="{button_id}" onclick="copyText('{content}')">
            <h4>{title}</h4>
            <p>{content}</p>
        </div>
    """, unsafe_allow_html=True)
