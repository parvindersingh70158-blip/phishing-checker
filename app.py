import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="wide")

# SIMPLE SAFE CSS - NO BG IMAGE
st.markdown("""
<style>
    #MainMenu, footer {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }
    .main-container {
        max-width: 800px;
        margin: 50px auto;
        padding: 40px;
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0,198,255,0.3);
        box-shadow: 0 8px 32px 0 rgba(0,198,255,0.2);
    }
    h1 {
        color: #00e5ff !important;
        text-align: center;
        font-size: 45px !important;
        text-shadow: 0 0 10px #00e5ff;
        margin-bottom: 10px !important;
    }
    .subtitle {
        color: #ccc !important;
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.4) !important;
        color: white !important;
        border: 2px solid #00c6ff !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 16px !important;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 40px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        width: 100%;
        margin-top: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px #00c6ff;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1>🔒 Phishing URL Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter any URL to verify if it is Safe or Phishing</p>', unsafe_allow_html=True)

url = st.text_input("URL", "https://google.com", label_visibility="collapsed")

def check_url(url):
    if not url:
        return "EMPTY"
    
    if not url.startswith("http"):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '').lower()
    
    # SAFE LIST
    trusted = ["google.com", "youtube.com", "facebook.com", "amazon.com", "github.com", "microsoft.com", "render.com", "netlify.com", "instagram.com"]
    
    if domain in trusted:
        return "SAFE"
    
    # PHISHING CHECKS
    score = 0
    if not url.startswith('https'): score += 3
    if "@" in url: score += 3
    if "-" in domain: score += 1
    if domain.count(".") > 3: score += 2
    if any(x in url.lower() for x in ["login","verify","account","bank","paypal","otp","update","secure"]): score += 2
    
    if score >= 3:
        return "PHISHING"
    return "SAFE"

if st.button("🚀 SCAN URL NOW"):
    result = check_url(url)
    
    if result == "EMPTY":
        st.warning("⚠️ Please enter a URL first")
    elif result == "SAFE":
        st.success("✅ THIS URL IS SAFE")
    elif result == "PHISHING":
        st.error("⚠️ THIS IS A PHISHING URL!")

st.markdown('</div>', unsafe_allow_html=True)
