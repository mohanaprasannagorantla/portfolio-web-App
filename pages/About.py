import streamlit as st


def app():
    # --- CUSTOM CSS STYLE ---
    st.markdown(
        """
        <style>
        /* Global Streamlit App Style overrides */
        .stApp {
            background: linear-gradient(180deg, #fdfefe 0%, #f4f7fc 100%);
            font-family: system-ui, -apple-system, sans-serif;
        }

        /* Glassmorphism containers with smooth hover elevation */
        .about-container, .section-box {
            padding: 24px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(226, 232, 240, 0.8);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            margin-bottom: 25px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .about-container:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.08);
            background: #ffffff;
        }
        
        /* Modern Profile header design with subtle zoom effect */
        .profile-header {
            text-align: center;
            margin-bottom: 35px;
            padding: 20px 0;
        }
        
        /* High-tech Gradient Text for your name */
        .profile-name {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            letter-spacing: -0.03em;
            margin-bottom: 8px;
            display: inline-block;
        }
        
        .profile-title {
            font-size: 1.25rem;
            color: #4b5563;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        /* Minimalist Modern Section titles */
        .section-title {
            color: #1e3a8a;
            font-weight: 700;
            padding-bottom: 8px;
            margin-top: 30px;
            margin-bottom: 20px;
            font-size: 1.6rem;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        /* Sleek Modern Interactive pill badges for tech stack */
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        
        .skill-badge {
            background-color: #f1f5f9;
            color: #1e293b;
            padding: 8px 16px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
            cursor: default;
        }
        
        .skill-badge:hover {
            background-color: #3b82f6;
            color: #ffffff;
            border-color: #3b82f6;
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }
        
        /* Enhanced Timeline tracker */
        .timeline-container {
            margin-bottom: 25px;
        }
        
        .timeline-item {
            margin-bottom: 0px;
            padding: 0px 0px 25px 24px;
            border-left: 2px solid #e2e8f0;
            position: relative;
        }
        
        /* Clean circle indicators replacing structural flat borders */
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -6px;
            top: 4px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: #3b82f6;
            border: 2px solid #ffffff;
            box-shadow: 0 0 0 2px #3b82f6;
            transition: background-color 0.2s ease;
        }
        
        .timeline-item:hover::before {
            background-color: #1e3a8a;
        }
        
        .timeline-item:last-child {
            border-left: 2px solid transparent;
            padding-bottom: 10px;
        }
        
        .timeline-date {
            font-size: 0.85rem;
            color: #3b82f6;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 4px;
        }
        
        .timeline-company {
            color: #4b5563;
            font-weight: 500;
        }
        
        .timeline-item p {
            color: #6b7280;
            margin-top: 6px;
            font-size: 0.95rem;
            line-height: 1.5;
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
            <div class="profile-title">🚀 Full Stack Developer</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- BIOGRAPHY ---
    st.markdown('<div class="section-title">💼 Professional Summary</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="about-container">
            Software Engineer with 8 years of professional experience,
            currently driving project success at Cognizant Technology Solutions. 
            Proven track record of developing and managing complex applications across diverse domains, 
            including E-Governance, Banking, and QFund. Expert in leveraging multiple modern frameworks
            and technologies to deliver scalable, high-quality software solutions.
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # --- WORK EXPERIENCE ---
    st.markdown('<div class="section-title">⏳ Experience</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline-container">
            <div class="timeline-item">
                <div class="timeline-date">2021 - Present</div>
                <strong>Senior Software Engineer</strong> — <span class="timeline-company">Cognizant Technology</span>
                <p>Working as a FullStack Application Developer to design scalable components.</p>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2019 - 2021</div>
                <strong>Software Engineer</strong> — <span class="timeline-company">Virinchi Technologies</span>
                <p>Worked as a Java FullStack Developer, handling multiple concurrent projects with diverse tech stacks.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # --- CORE SKILLS SECTION ---
    # Fixed broken tags by unifying the section headers cleanly
    st.markdown('<div class="section-title">⚡ Core Skills</div>', unsafe_allow_html=True)
    
    skills = ["Java", "Spring", "JavaScript", "SpringBoot", "SQL", "Microservices", "OCP", "Hibernate", "Docker", "Kubernetes", "AWS", "Python", "Data Science", "Git"]
    skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
    
    st.markdown(
        f"""
        <div class="section-box">
            <div class="skills-container">{skills_html}</div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- EDUCATION ---
    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline-container">
            <div class="timeline-item">
                <div class="timeline-date">2008 - 2011</div>
                <strong>Master of Computer Application (MCA)</strong> — <span class="timeline-company">JNTU University</span>
                <p>Graduated with a focus on advanced database management and software engineering methodologies.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Testing execution entry-point
if __name__ == "__main__":
    st.set_page_config(page_title="About Me", layout="centered")
    app()