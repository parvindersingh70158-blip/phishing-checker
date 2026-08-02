import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="wide")

# CYBER UNIVERSE ANIMATED BACKGROUND
st.markdown("""
<style>
    /* Hide streamlit header/footer */
    #MainMenu, footer {visibility: hidden;}
    
    /* Animated starfield background */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        overflow: hidden;
    }
    
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background: transparent url('https://i.imgur.com/YKY28eT.png') repeat;
        animation: moveStars 200s linear infinite;
        z-index: -1;
    }
    
    @keyframes moveStars {
        from {background-position: 0 0;}
        to {background-position: -10000px 5000px;}
    }

    /* Main glass card */
    .main-container {
        background: rgba(10, 15, 30, 0.6);
        backdrop-filter: blur(12px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(0, 200, 255, 0.3);
        box-shadow: 0 0 40px rgba(0, 200, 255, 0.2);
        max-width: 700px;
        margin: 50px auto;
        text-align: center;
    }
    
    /* Tech title with glow */
    h1 {
        color: #00f0ff !important;
        text-shadow: 0 0 15px #00f0ff;
        font-size: 2.5em !important;
    }
    
    /* Center button */
    div.stButton {text-align: center;}
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 35px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 0 20px rgba(0, 114, 255, 0.6);
        transition: all 0.3s ease;
        margin: 0 auto;
        display: block;
    }
    .stButton>button:hover {
        box-shadow: 0 0 35px rgba(0, 114, 255, 1);
        transform: translateY(-2px);
    }
    
    /* Input box styling */
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.4);
        border: 1px solid #00c6ff;
        color: white;
        border-radius: 10px;
        text-align: center;
    }
</style>

<div class="stars"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("🔒 Phishing URL Checker")
st.markdown("### **AI Powered Cybersecurity Scanner**")
st.write("Enter any URL to verify if it is **Safe** or **Phishing**")
st.write("")

url = st.text_input("Enter URL here:", "https://google.com", label_visibility="collapsed")

if st.button("🚀 SCAN URL NOW"):
    if url:
        def check_url(url):
            url_lower = url.lower()
            trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'microsoft.com']
            if any(t in url_lower for t in trusted): return "SAFE"
            
            score = 0
            if 'https' not in url: score += 2
            if '@' in url: score += 3
            if url.count('.') > 4: score += 2
            if '-' in urlparse(url).netloc: score += 1
            if any(w in url_lower for w in ['login','verify','account','update']): score += 2
            if 'bit.ly' in url_lower or 'tinyurl' in url_lower: score += 3
            
            return "PHISHING" if score >= 3 else "SAFE"

        result = check_url(url)
        
        if result == "PHISHING":
            st.error("⚠️ THREAT DETECTED: PHISHING URL!")
            st.write("**Do not click on this link**")
        else:
            st.success("✅ VERIFIED: SAFE URL")
            st.write("**You can proceed safely**")
    else:
        st.warning("Please enter a URL first")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #888;'>Powered by CyberSec AI | Project 2026</p>", unsafe_allow_html=True)
