import streamlit as st

st.set_page_config(page_title="portfolio",layout="wide")
# 2. Function to Load Custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")
col1,col2=st.columns([1,2],border=True)
with col1:
    st.image("assests/image.jpg",width=150,caption="Radhika")
with col2:
    st.title("Radhika")
    st.subheader ("software engineer")
    st.write("""
             this is  my portfolio 
            Java Fullstack Expert ||
            DataScience Analist 
               """)
    st.download_button("Here is my resume",open("assests/resume.pdf","rb"),file_name="resume.pdf")
    st.divider()
    c1,c2,c3=st.columns(3)
    with c1:
        st.metric("Experience","8")
    with c2:
        st.metric("Companies Worked","4")
    with c3:
        st.metric("Projects Handled","10") 
            
