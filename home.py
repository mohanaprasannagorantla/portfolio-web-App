import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="My Portfolio | Home",
    page_icon="💼",
    layout="wide",
)

# 2. Inject Custom CSS Styling
st.markdown(
    """
    <style>
    /* Main container background and text color */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Hero section tracking card */
    .hero-container {
        padding: 2.5rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
    }
    
    /* Gradient text for main header */
    .hero-title {
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle styling */
    .hero-subtitle {
        font-size: 1.5rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }
    
    /* Quick stats card container */
    .stat-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #38bdf8;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #38bdf8;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #94a3b8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Hero Section (With Image & Resume Layout)
hero_col1, hero_col2 = st.columns([1, 3])

with hero_col1:
    # Placed profile image in the left column
    st.image("assests/image.jpg",width=150,caption="Radhika")
    
    # Safely opens and loads the resume file for download
     
    try:
      st.download_button("Here is my resume",open("assests/resume.pdf","rb"),file_name="resume.pdf")
    except FileNotFoundError:
        st.warning("Resume file not found in 'assets/' folder.")

with hero_col2:
    # Text profile elements placed in the right column
    st.markdown(
        """
        <div class="hero-container">
            <h1 class="hero-title">Hello, I'm Radhika</h1>
            <p class="hero-subtitle">Full Stack Developer </p>
            <p style="color: #cbd5e1;">
                This is  my portfolio  am expert in  developing web based applications with  mutiple techonologies like
            Java ,Python, Redhat Openshift ,Spring ,SpringBoot , Microservices
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("---")

# 4. Key Metrics / Stats Section
st.subheader("🚀 At a Glance")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">8+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">10+</div>
            <div class="stat-label">Projects Completed</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">12</div>
            <div class="stat-label">Open Source Tools</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.write("---")

# 5. Core Expertise Section
st.subheader("💡 Core Expertise")
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### 🛠️ Tech Stack")
    st.write("**Languages:** Python, JavaScript, Java, SQL, ")
    st.write("**Frameworks:** Streamlit, RestFull webservice, Spring MVC,IO,SpringBoot,MicroServices")
    st.write("**Cloud & DevOps:** AWS, Docker, GitHub Actions, PostgreSQL")

with right_col:
    st.markdown("### 🎯 What I Do")
    st.markdown("- **Web Development:** Creating interactive, responsive web applications.")
    st.markdown("- **Data Engineering:** Building pipeline automation and real-time dashboards.")
    st.markdown("- **API Integration:** Deploying robust backend microservices.")

st.write("---")

# 6. Call to Action / Footer
st.markdown("### 🤝 Let's Connect")
st.write("Feel free to reach out for collaborations or freelance opportunities!")

st.sidebar.success("Select a page above to view projects or contact details.")