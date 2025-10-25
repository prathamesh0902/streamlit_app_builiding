import streamlit as st
import pandas as pd

# --- Title & Description ---
st.title("🚀 My First Streamlit App")
st.write("This is a simple demo app built with Streamlit!")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ File uploaded successfully!")
    st.dataframe(df.head())

    # --- Basic Stats ---
    st.subheader("📊 Data Summary")
    st.write(df.describe())
else:
    st.info("Please upload a CSV file to get started.")


