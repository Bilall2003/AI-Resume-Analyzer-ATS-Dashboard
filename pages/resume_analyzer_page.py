import streamlit as st

st.title("Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")