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
    <!-- Import Google Font -->
    <style>
    @import url('https://googleapis.com');
    
    /* Apply globally to Streamlit app */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero container with micro-shadow */
    .hero-container {
        padding: 2.5rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    
    /* Fixed Syntax for Gradient Text */
    .hero-title {
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 0.5rem;
        display: inline-block;
    }
    
    /* Subtitle styling */
    .hero-subtitle {
        font-size: 1.5rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }
    
    /* Quick stats card container + Hover Effects */
    .stat-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 12px;
        border-top: 4px solid #38bdf8; /* Swapped to top border */
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(56, 189, 248, 0.15);
    }
    
    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #38bdf8;
    }
    
    .stat-label {
        font-size: 0.95rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Target Native Streamlit Download Button */
    div.stDownloadButton > button {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.2s ease-in-out !important;
        width: 100%;
    }

    div.stDownloadButton > button:hover {
        background-color: #818cf8 !important;
        color: #ffffff !important;
        transform: scale(1.03);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Hero Section (With Image & Resume Layout)
hero_col1, hero_col2 = st.columns([1, 2.5], gap="large")

with hero_col1:
    # 1. Custom CSS wrapper to make any native Streamlit image circular
    st.markdown(
        """
        <style>
        /* Target the image element inside column 1 */
        [data-testid="stImage"] img {
            border-radius: 50% !important;
            border: 4px solid #38bdf8 !important;
            object-fit: cover !important;
            height: 150px !important;
            width: 150px !important;
        }
        /* Style the native Streamlit caption underneath */
        [data-testid="stImageCaption"] {
            color: #f8fafc !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            text-align: center !important;
            margin-top: 10px !important;
            margin-bottom: 20px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 2. Your exact line of code inserted here
    st.image("assests/image.jpg", width=150, caption="Radhika")
    
    # 3. Safely opens and loads the resume file for download
    try:
        with open("assests/resume.pdf", "rb") as file:
            st.download_button("Download Resume", data=file, file_name="resume.pdf")
    except FileNotFoundError:
        st.warning("Resume file not found in 'assests/' directory.")
with hero_col2:
    # Using your HTML structures inside the right layout column
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-title">Hello, I'm Radhika</div>
            <div class="hero-subtitle">Full Stack Developer </div>
            <p style="color: #cbd5e1; line-height: 1.6;">
                This is  my portfolio  am expert in  developing web based applications with  mutiple techonologies like
            Java ,Python, Redhat Openshift ,Spring ,SpringBoot , Microservices
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    

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