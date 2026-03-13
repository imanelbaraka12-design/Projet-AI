import streamlit as st
from cv_screening_agent import analyze_cv

st.title("AI CV Screening Agent")

uploaded_file = st.file_uploader("Upload a CV", type=["pdf","txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    result = analyze_cv(text)
    
    st.write("Résultat de l'analyse :")
    st.write(result)
