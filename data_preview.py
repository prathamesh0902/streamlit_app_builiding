import streamlit as st
import pandas as pd

st.title("📊 Data Preview App")

# Load data stored in the same folder
@st.cache_data
def load_data():
    df = pd.read_csv("sample_data.csv")   # file in same GitHub repo
    return df

df = load_data()
st.dataframe(df.head())
