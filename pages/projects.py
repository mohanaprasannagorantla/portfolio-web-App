import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="My Portfolio | Projects",
    page_icon="💼",
    layout="wide"
)

# 2. Custom CSS Styling
custom_css = """
<style>
    @import url('https://googleapis.com');

    /* Fixed global app background override */
    .stApp {
        background: linear-gradient(180deg, #fdfefe 0%, #f4f7fc 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Elegant Header Gradient Styling */
    .header-title {
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #4F46E5 0%, #06B6D4 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 4px;
        letter-spacing: -0.03em;
    }

    .header-subtitle {
        font-size: 1.15rem;
        color: #475569;
        margin-bottom: 30px;
    }
    
    /* Unified Project Card with Glassmorphism Elevation */
    .project-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(8px);
        padding: 28px;
        border-radius: 16px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 25px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Smooth 3D Hover Lift and Highlight Glow */
    .project-card:hover {
        transform: translateY(-4px);
        background: #ffffff;
        box-shadow: 0 20px 25px -5px rgba(79, 70, 229, 0.08), 0 10px 10px -5px rgba(79, 70, 229, 0.04);
        border-color: #4F46E5;
    }
    
    /* Project Title with Interactive Accent */
    .project-title {
        color: #0F172A;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 12px;
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Sleek Tech Stack Badges with Interactive Glow */
    .tech-badge {
        display: inline-block;
        background-color: #EEF2F6;
        color: #4F46E5;
        padding: 5px 12px;
        border-radius: 9999px;
        font-size: 13px;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 10px;
        border: 1px solid #E2E8F0;
        transition: all 0.2s ease;
    }

    .tech-badge:hover {
        background-color: #4F46E5;
        color: #ffffff;
        border-color: #4F46E5;
    }
    
    /* Formatted Project Description Text */
    .project-desc {
        color: #475569;
        font-size: 15.5px;
        line-height: 1.7;
        margin-top: 12px;
        text-align: justify;
        white-space: pre-line; /* Keeps your multiline formatting working beautifully */
    }

    /* Target Native Streamlit Link Buttons globally to style them into clean code cards */
    div.stLinkButton > a {
        background-color: #ffffff !important;
        color: #4F46E5 !important;
        border: 2px solid #E2E8F0 !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    }

    div.stLinkButton > a:hover {
        background-color: #4F46E5 !important;
        color: #ffffff !important;
        border-color: #4F46E5 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2) !important;
    }
</style>
"""
# Injecting the CSS
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<h1 class="header-title">📂 My Projects</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-subtitle">A comprehensive showcase of my engineering and software development portfolio.</p>', unsafe_allow_html=True)

# 4. Project Data Dictionary
projects = [
    {
        "title": "Overview of All My Projects",
        "desc": "In my entire career, I have handled, designed, and developed multiple projects across different technologies. Here is a curated selection highlighting core production systems.",
        "tech": ["Java","JDBC","Servlets", "JSP","Struts","MySQL" , "RESTful Web Services", "Hibernate","Spring", "Spring Boot"] ,
        "link": "https://github.com"               
    },
    {
        "title": "Discover Financial Services",
        "tech": ["AWS", "SpringBoot", "Kafka", "Java","OCP","Docker","Kubernetes","Jenkins Pipeline","Microservices"],
        "desc": "A heavy financial banking domain system engine providing multi-tiered credit card transaction architectures, personal lines of credit, student loan distribution pipelines, and asset optimization channels.",
        "link": "https://github.com"
    },
    {
        "title": "VCard (Indianization System)",
        "tech": ["Java","JDBC","Servlets", "JSP","Struts" ,"MySQL" , "RESTful Web Services"],
        "desc": """The VCard Management System is a comprehensive platform engineered to automate complete core internal Card Processing lifecycle activities for financial institutions. It provides native infrastructure suitable for processing scale debit, credit, and microchip smart cards.

        Key Architectural Delivery:
        • High-throughput API engines running customer provisioning pipelines (Registration, Payments, Balances).
        • Background micro-schedulers parsing transaction statements into dynamic accounting logs.
        • Integrated visualization loops projecting financial insights with high-performance reporting charts.""",
        "link": "https://github.com"
    },
    {
        "title": "Degree Online Services, Telangana (DOST)",
        "tech": ["JSP", "Servlets", "JDBC" ,"Struts", "PostgreSQL", "Tomcat", "Ajax", "JavaScript"],
        "desc": """An enterprise-scale Web Admissions system handling high-concurrency undergraduate university processing workflows across Telangana state.

        The infrastructure provides a streamlined ecosystem letting students securely evaluate course mapping, filter institution profiles based on geographical matrix locations, and manage academic selection algorithms safely.""",
        "link": "https://github.com"
    }
]

# 5. Rendering Layout using Columns
for project in projects:
    # 3:1 spatial grid separating content from active hyperlink columns
    col1, col2 = st.columns([3.5, 1], gap="medium")
    
    with col1:
        # Generate tech stack HTML string
        badges_html = "".join([f'<span class="tech-badge">{tech}</span>' for tech in project["tech"]])
        
        # Render the custom CSS card container
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-title">⚡ {project['title']}</div>
                <div style="margin-bottom: 4px;">{badges_html}</div>
                <p class="project-desc">{project['desc']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col2:
        # Visual spatial spacing logic alignment blocks
        st.write(" ") 
        st.write(" ")
        st.write(" ")
        st.link_button("Code Metrics 🔗", project["link"], use_container_width=True)
    
    st.write("") # Layout delimiter element spacer loop step
