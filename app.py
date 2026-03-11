import numpy as np
import streamlit as st
import matplotlib

st.title("hekko")

cv=st.file_uploader("Drop your CV")
if cv:
    st.balloons()
