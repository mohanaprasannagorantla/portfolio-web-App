import streamlit as st


def app():
    # --- CUSTOM CSS STYLE ---
    st.markdown(
        """
        <style>
        /* Main container styling */
        .about-container {
            padding: 20px;
            border-radius: 10px;
            background-color: #f8f9fa;
            margin-bottom: 25px;
        }
        
        /* Profile section */
        .profile-header {
            text-align: center;
            margin-bottom: 30px;
        }
        .profile-name {
            font-size: 2.5rem;
            color: #1E3A8A;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .profile-title {
            font-size: 1.2rem;
            color: #4B5563;
            font-style: italic;
        }
        
        /* Section headers */
        .section-title {
            color: #1E3A8A;
            border-bottom: 2px solid #3B82F6;
            padding-bottom: 5px;
            margin-top: 20px;
            margin-bottom: 15px;
            font-size: 1.5rem;
        }
        /* Skills layout */
            .skills-container {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 10px;
            }
            .skill-badge {
                background-color: #EAECEE;
                color: #34495E;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: 500;
            }
        
        /* Timeline items */
        .timeline-item {
            margin-bottom: 15px;
            padding-left: 15px;
            border-left: 3px solid #3B82F6;
        }
        .timeline-date {
            font-size: 0.85rem;
            color: #6B7280;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- PROFILE HEADER ---
    st.markdown(
        """
        <div class="profile-header">
            <div class="profile-name">Radhika Medakayala</div>
            <div class="profile-title">Full Stack Developer </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- BIOGRAPHY ---
    st.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="about-container">
            Software Engineer with 8 years of professional experience,
          currently driving project success at Cognizant Technology Solutions. 
         Proven track record of developing and managing complex applications across diverse domains, 
         including E-Governance, Banking, and QFund. Expert in leveraging multiple modern frameworks
          and technologies to deliver scalable, high-quality software solutions 
        </div>
        """,
        unsafe_allow_html=True,
    )
    # --- WORK EXPERIENCE ---
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline-item">
            <div class="timeline-date">2021 - Present</div>
            <strong>Senior Software Engineer</strong> — Cognizant Technology
            <p>working as a FullStack Application Developer .</p>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">2019 - 2021</div>
            <strong>Software Engineer</strong> — Virinchi Technologies
            <p>worked as a Java FullStack Developer and handling multiple projects with different Technologies</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
# Core Skills Section
    st.markdown('<div class="section-box"><h3 class="section-title">⚡ Core Skills</h3>', unsafe_allow_html=True)
    
    skills = ["Java", "Spring", "JavaScript", "SpringBoot", "SQL", "Microservicess", "OCP","Hibernate","Dockers","Kubernates","AWS", "Python","DataScience","Git"]
    skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
    
    st.markdown(f'<div class="skills-container">{skills_html}</div></div>', unsafe_allow_html=True)

    # --- EDUCATION ---
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline-item">
            <div class="timeline-date">2008 - 2011</div>
            <strong>Master of Computer Application(MCA)</strong> — JNTU University
            <p>Graduated in Masters in Computer Applications</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    


# This allows running the file individually for testing
if __name__ == "__main__":
    st.set_page_config(page_title="About Me", layout="centered")
    app()