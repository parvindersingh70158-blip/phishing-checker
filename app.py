import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="wide")

# ANIMATED TECH BACKGROUND CSS
st.markdown("""
<style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #0f2027);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glass effect for main container */
    .main-container {
        background: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(0, 255, 255, 0.2);
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.1);
    }
    
    /* Tech glow for title */
    h1 {
        color: #00ffff !important;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
    }
    
    /* Button glow */
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(0, 114, 255, 0.5);
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(0, 114, 255, 0.8);
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("🔒 Phishing URL Checker")
st.write("### AI Powered Cybersecurity Tool")
st.write("Enter any URL to check if it is **Safe** or **Phishing**")

def check_url(url):
    url_lower = url.lower()
    
    # Trusted websites
    trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'microsoft.com']
    if any(t in url_lower for t in trusted):
        return "SAFE"
    
    score = 0
    if 'https' not in url: score += 2
    if '@' in url: score += 3
    if url.count('.') > 4: score += 2
    if '-' in urlparse(url).netloc: score += 1
    if 'login' in url_lower or 'verify' in url_lower or 'account' in url_lower: score += 2
    if 'bit.ly' in url_lower or 'tinyurl' in url_lower: score += 3
    if 'bank' in url_lower or 'paypal' in url_lower: score += 2
    
    if score >= 3:
        return "PHISHING"
    else:
        return "SAFE"

url = st.text_input("Enter URL here:", "https://google.com")

if st.button("Scan URL Now"):
    if url:
        result = check_url(url)
        
        if result == "PHISHING":
            st.error("⚠️ THREAT DETECTED: PHISHING URL!")
            st.write("Do not click on this link")
        else:
            st.success("✅ VERIFIED: SAFE URL")
            st.write("You can proceed safely")
    else:
        st.warning("Please enter a URL first")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Powered by Cybersecurity AI | Project 2026")
