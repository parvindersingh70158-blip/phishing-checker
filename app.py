vimport streamlit as st
from urllib.parse import urlparse
import random

st.set_page_config(page_title="Phishing URL Checker", layout="centered")

# ANIMATED WALLPAPER + PARTICLES CSS
st.markdown("""
<style>
    #MainMenu, footer {visibility: hidden;}
    
    /* ANIMATED GRADIENT BG */
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f2027);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        overflow: hidden;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    /* FLOATING PARTICLES */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
    }
    .particle {
        position: absolute;
        bottom: -10px;
        background: rgba(0, 198, 255, 0.5);
        border-radius: 50%;
        box-shadow: 0 0 10px #00c6ff;
        animation: rise linear infinite;
    }
    @keyframes rise {
        from {transform: translateY(0) scale(0); opacity: 0;}
        10% {opacity: 1;}
        90% {opacity: 1;}
        to {transform: translateY(-110vh) scale(1); opacity: 0;}
    }
    
    /* MAIN BOX */
    .main-box {
        position: relative;
        z-index: 1;
        max-width: 850px;
        margin: 80px auto;
        padding: 40px;
        background: rgba(5, 5, 20, 0.7);
        border-radius: 20px;
        border: 1px solid rgba(0, 198, 255, 0.4);
        backdrop-filter: blur(15px);
        box-shadow: 0 0 50px rgba(0, 198, 255, 0.3);
    }
    h1 {
        color: #00e5ff !important;
        font-size: 42px !important;
        text-align: center;
        text-shadow: 0 0 20px #00e5ff;
        margin-bottom: 15px !important;
    }
    .subtitle {
        color: #c0c0ff !important;
        text-align: center;
        font-size: 16px !important;
        margin-bottom: 30px !important;
    }
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.5) !important;
        color: #ffffff !important;
        border: 2px solid #00c6ff !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        font-size: 15px !important;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 40px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        width: 100%;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 198, 255, 0.5);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 35px rgba(0, 198, 255, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# GENERATE 50 PARTICLES
particles_html = '<div class="particles">'
for i in range(50):
    size = random.randint(2, 5)
    left = random.randint(0, 100)
    duration = random.randint(10, 25)
    delay = random.randint(0, 15)
    particles_html += f'<div class="particle" style="width:{size}px; height:{size}px; left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;"></div>'
particles_html += '</div>'
st.markdown(particles_html, unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1>🔒 Phishing URL Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter any URL to verify if it is Safe or Phishing</p>', unsafe_allow_html=True)

url = st.text_input("URL", "", label_visibility="collapsed", placeholder="https://example.com")

def check_url(url):
    if not url:
        return "EMPTY"
    
    if not url.startswith("http"):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '').lower()
    url_lower = url.lower()
    
    # 1. SAFE LIST
    trusted = ["google.com", "youtube.com", "facebook.com", "amazon.com", "github.com", "microsoft.com", "render.com", "instagram.com"]
    if domain in trusted:
        return "SAFE"
    
    # 2. DIRECT PHISHING SIGNS
    phishing_keywords = ["login","verify","account","bank","paypal","otp","secure","update","confirm","password"]
    suspicious_tld = [".tk", ".ml", ".ga", ".cf", ".gq"]
    
    if any(word in url_lower for word in phishing_keywords):
        return "PHISHING"
    if any(domain.endswith(tld) for tld in suspicious_tld):
        return "PHISHING"
    if "@" in url:
        return "PHISHING"
    if not url.startswith('https'):
        return "PHISHING"
    
    # 3. BAAT SAB NORMAL SAFE
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
