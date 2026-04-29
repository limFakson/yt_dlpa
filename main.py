import streamlit as st
import subprocess

st.title("Stickie")

url = st.text_input("Enter Youtube URL")
st.segmented_control("", ["Check info", "Convert"], selection_mode="multi")

