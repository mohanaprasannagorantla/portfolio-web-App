import streamlit as st

# Configure page settings
st.set_page_config(page_title="Contact Me", page_icon="✉️", layout="centered")

# Custom CSS for styling the contact page
custom_css = """
<style>
    @import url('https://googleapis.com');

    /* Global configuration adjustment override */
    .stApp {
        background: linear-gradient(180deg, #fdfefe 0%, #f4f7fc 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Premium Title Header styling with gradient accent */
    .contact-header {
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 8px;
        text-align: center;
        letter-spacing: -0.03em;
    }
    
    /* Subtitle layout */
    .contact-subtitle {
        font-size: 1.15rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 45px;
        font-weight: 400;
    }
    
    /* Upgraded Modern Information Cards */
    .info-card-container {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    .info-card-item {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(8px);
        padding: 16px 20px;
        border-radius: 12px;
        border: 1px solid rgba(229, 231, 235, 0.7);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        display: flex;
        align-items: center;
        gap: 14px;
        transition: all 0.2s ease-in-out;
    }
    
    .info-card-item:hover {
        transform: translateX(4px);
        background: #ffffff;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        border-color: #3B82F6;
    }

    .info-icon {
        font-size: 1.5rem;
        background: #eff6ff;
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
    }

    .info-details {
        display: flex;
        flex-direction: column;
    }

    .info-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        font-weight: 600;
    }

    .info-value a {
        color: #1E3A8A !important;
        text-decoration: none !important;
        font-weight: 600;
    }
    .info-value p {
        margin: 0;
        color: #1F2937;
        font-weight: 600;
    }
    
    /* Target Native Streamlit form container */
    div[data-testid="stForm"] {
        border: 1px solid rgba(229, 231, 235, 0.8) !important;
        padding: 32px !important;
        border-radius: 16px !important;
        background-color: #FFFFFF !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02) !important;
    }

    /* Polish Form Submission Button directly via Streamlit HTML mapping */
    div[data-testid="stForm"] button {
        background-color: #1E3A8A !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.6rem 2rem !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }

    div[data-testid="stForm"] button:hover {
        background-color: #3B82F6 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
</style>
"""

# Inject CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Render Styled Headers using HTML strings
st.markdown('<div class="contact-header">Get In Touch</div>', unsafe_allow_html=True)
st.markdown('<div class="contact-subtitle">Have a question or want to work together? Drop a message below!</div>', unsafe_allow_html=True)

# Create layout splits: Left for Info, Right for Form
col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("Contact Information")
    
    # Combined HTML card tray layout
    st.markdown(
        """
        <div class="info-card-container">
            <div class="info-card-item">
                <div class="info-icon">📍</div>
                <div class="info-details">
                    <span class="info-label">Location</span>
                    <span class="info-value"><p>Hyderabad, India</p></span>
                </div>
            </div>
            <div class="info-card-item">
                <div class="info-icon">✉️</div>
                <div class="info-details">
                    <span class="info-label">Email</span>
                    <span class="info-value"><a href="mailto:radhika7284@gmail.com">radhika7284@gmail.com</a></span>
                </div>
            </div>
            <div class="info-card-item">
                <div class="info-icon">🔗</div>
                <div class="info-details">
                    <span class="info-label">LinkedIn</span>
                    <span class="info-value"><a href="https://www.linkedin.com/in/radhika-medakayala-78654785/" target="_blank">View Profile</a></span>
                </div>
            </div>
            <div class="info-card-item">
                <div class="info-icon">💻</div>
                <div class="info-details">
                    <span class="info-label">GitHub</span>
                    <span class="info-value"><a href="https://github.com/mohanaprasannagorantla/" target="_blank">View Projects</a></span>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    

with col2:
    st.subheader("Send a Message")
    
    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("Full Name", placeholder="Radhika Medakayala")
        email = st.text_input("Email Address", placeholder="radhika7284@gmail.com")
        subject = st.text_input("Subject", placeholder="Project Inquiry")
        message = st.text_area("Your Message", placeholder="Type your message here...", height=150)
        
        # Submit button
        submit_button = st.form_submit_button(label="Send Message")
        
        if submit_button:
            if not name or not email or not message:
                st.error("Please fill out all required fields (Name, Email, Message).")
            elif "@" not in email:
                st.error("Please enter a valid email address.")
            else:
                # Process messages or handle Formspree endpoint requests here
                st.success(f"Thank you, {name}! Your message has been sent successfully.")