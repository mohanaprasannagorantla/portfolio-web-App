import streamlit as st
st.write("## Projects")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Project 1: Data Dashboard")
    st.write("An interactive dashboard built using Streamlit and Pandas to analyze global financial trends.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Project 2: Machine Learning API")
    st.write("A predictive model deployed via FastAPI and Streamlit to forecast housing prices.")
    st.markdown("</div>", unsafe_allow_html=True)