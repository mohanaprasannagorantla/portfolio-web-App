import streamlit as st

# Configure page settings
st.set_page_config(page_title="Contact Me", page_icon="✉️", layout="centered")

# Custom CSS for styling the contact page
custom_css = """
<style>
    /* Style the main container */
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .contact-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #1E3A8A; /* Deep blue */
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 10px;
        text-align: center;
    }
    
    /* Subtitle styling */
    .contact-subtitle {
        font-size: 18px;
        color: #4B5563; /* Muted gray */
        text-align: center;
        margin-bottom: 40px;
    }
    
    /* Card wrapper for contact info */
    .info-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 20px;
    }
    
    .info-card h4 {
        margin: 0 0 5px 0;
        color: #1E3A8A;
    }
    
    .info-card p {
        margin: 0;
        color: #374151;
    }
    
    /* Target Streamlit form inputs for subtle customization */
    div[data-testid="stForm"] {
        border: 1px solid #E5E7EB;
        padding: 30px;
        border-radius: 12px;
        background-color: #FFFFFF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
</style>
"""

# Inject CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Render Styled Headers using HTML strings
st.markdown('<div class="contact-header">Get In Touch</div>', unsafe_allow_html=True)
st.markdown('<div class="contact-subtitle">Have a question or want to work together? Drop a message below!</div>', unsafe_allow_html=True)

# Create layout splits: Left for Info, Right for Form
col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("Contact Information")
    
    # Render custom styled information cards
    st.markdown("📍 **Location:** Hyderabad, India")
    st.markdown("✉️ **Email:** radhika7284@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/radhika-medakayala-78654785/) ")
    st.markdown(" [GitHub]( https://github.com/mohanaprasannagorantla/)")
    

with col2:
    st.subheader("Send a Message")
    
    # Use Formspree (or any endpoint) for real email delivery backend, or process locally
    # Replace 'your_formspree_id' with your actual Formspree ID to make it work out-of-the-box
    formspree_url = "https://formspree.io" 
    
    # HTML Form wrapper instead of st.form to easily handle external POST actions if desired.
    # Alternatively, you can use native st.form as shown below:
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
                # Backend processing logic goes here (e.g., sending emails via smtplib, webhook, or saving to database)
                st.success(f"Thank you, {name}! Your message has been sent successfully.")