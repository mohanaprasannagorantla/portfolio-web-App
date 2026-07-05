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
    /* Main background and text alignment */
    .reportview-container {
        background-color: #f5f7f8;
    }
    
    /* Project Card Styling */
    .project-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        border-left: 5px solid #4F46E5;
        transition: transform 0.2s ease;
    }
    
    /* Card Hover Effect */
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    /* Project Title styling */
    .project-title {
        color: #1E293B;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    /* Tech Stack Badges */
    .tech-badge {
        display: inline-block;
        background-color: #EEF2F6;
        color: #4F46E5;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 12px;
    }
    
    /* Project Description */
    .project-desc {
        color: #475569;
        font-size: 15px;
        line-height: 1.6;
    }
</style>
"""
# Injecting the CSS
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Header Section
st.title("📂 My Projects")
st.markdown("A comprehensive showcase of my engineering and software development portfolio.")
st.write("---")

# 4. Project Data Dictionary
projects = [
    
    {
        "title": "⚡ Overview of All MY projects",
        "desc": " In My Entire Career handling,designed,developed multiple Projects with diffferent technologies.Here mention few of them",
        "tech": ["Java","JDBC","Servlets", "Jsp","Structs","Mysql" , "RestFul web Services", "Hibernate"," Spring", "Spring Boot"] ,
          "link": "https://github.com"               
        
    },
    {
        "title": "⚡Discover Financial Services ",
        "tech": ["AWS", "SpringBoot", "kafka", "Java","OCP","Docker","Kubernats","JenkinsPipline","Microservices"],
        "desc": "It is Banking Domain project. it provifdes different types of credit card services,Home Loans,personal Loans,student Loans",
        "link": "https://github.com"
    },
    {
        "title": "⚡ VCard(Indianization)",
        "tech": ["Java","JDBC","Servlets", "Jsp","Structs" ,"Mysql" , "RestFul web Services"],
        "desc": """The VCard Management System is a Windows based
                        application that takes care of the complete internal Card
                        Processing activities of a Bank (management and maintenance
                        of cards). It is suitable for the management of Debit Cards,
                        Credit Cards as well as Smart Cards. It mainly provide the API
                        Services of customer like Registration Of
                        Customer,MakePayment,LoanTransction,LoanTransc
                        tion By statement these all API Services are included in this project.
                        VCard provides vast functionality for MoneyLender's
                        companies to automate various
                        categories like
                        To generate Monthly statement by using schedulers.
                        To Display the monthly statement generation by using jfreeCharts
                        Api & KnownXChart Api.
                        For Monthly""",
        "link": "https://github.com"
    },
    {
        "title": "⚡ Degree Online Services, Telangana (DOST)",
        "tech": ["JSP", "Servlets", "Jdbc" ,"Struts", "PostgreeSql", "Tomcat", "Ajax", "JavaScript"],
        "desc":  """Degree Online Services, Telangana (DOST) is an Web Based
                application for the online admissions for undergraduate courses,
                through this online service the students knows the courses details
                with colleges wise affiliated under Universities available in
                Telangana State who are joined in under graduate courses.
                DOST is a friendly and effortless way to apply for
                undergraduate course. DOST helps you in choosing your favourite
                undergraduate course with all the information you wish to
                have.DOST minimizes your efforts and maximizes your choices to
                opt for an undergraduate course.
        """,
        "link": "https://github.com"
    }
]

# 5. Rendering Layout using Columns
for index, project in enumerate(projects):
    # Standard Streamlit columns for side-by-side spacing if needed
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Generate tech stack HTML string
        badges_html = "".join([f'<span class="tech-badge">{tech}</span>' for tech in project["tech"]])
        
        # Render the custom CSS card container
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-title">{project['title']}</div>
                <div>{badges_html}</div>
                <p class="project-desc">{project['desc']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col2:
        # Placing standard Streamlit interaction buttons alongside the custom HTML cards
        st.write(" ") # Spacer
        st.write(" ")
        st.link_button("View Source Code 🔗", project["link"], use_container_width=True)
    
    st.write("") # Tiny spacer between rows