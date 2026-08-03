import streamlit as st
from urllib.parse import urlparse
import random

st.set_page_config(page_title="Phishing URL Checker", layout="centered")

# BG NEELA + PARTICLES - AB BLACK NAHI HOGA
st.markdown("""
<style>
    #MainMenu, footer {visibility: hidden;}
    
    /* NEELA BG - BLACK HATA DIYA */
    .stApp {
        background: linear-gradient(180deg, #0a0a30 0%, #1a1a50 100%);
        overflow: hidden;
    }
    
    /* PARTICLES */
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
        background: #00ffff;
        border-radius: 50%;
        box-shadow: 0 0 10px #00ffff;
        animation: rise linear infinite;
    }
    @keyframes rise {
        from {transform: translateY(0); opacity: 0;}
        10% {opacity: 1;}
        90% {opacity: 1;}
        to {transform: translateY(-110vh); opacity: 0;}
    }
    
    /* MAIN BOX */
    .main-box {
        position: relative;
        z-index: 1;
        max-width: 800px;
        margin: 80px auto;
        padding: 40px;
        background: rgba(0, 0, 20, 0.8);
        border-radius: 20px;
        border: 2px solid #00ffff;
        backdrop-filter: blur(10px);
    }
    h1 {
        color: #00ffff !important;
        font-size: 40px !important;
        text-align: center;
        text-shadow: 0 0 15px #00ffff;
    }
    .subtitle {
        color: #ffffff !important;
        text-align: center;
        font-size: 16px !important;
        margin-bottom: 30px !important;
    }
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.7) !important;
        color: #ffffff !important;
        border: 2px solid #00ffff !important;
        border-radius: 10px !important;
        padding: 14px !important;
        text-align: center;
        font-size: 15px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00ffff, #0088ff) !important;
        color: black !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        width: 100%;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 40 PARTICLES
particles_html = '<div class="particles">'
for i in range(40):
    size = random.randint(3, 6)
    left = random.randint(0, 100)
    duration = random.randint(8, 20)
    delay = random.randint(0, 10)
    particles_html += f'<div class="particle" style="width:{size}px; height:{size}px; left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;"></div>'
particles_html += '</div>'
st.markdown(particles_html, unsafe_allow_html=True)


st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1>🔒 Phishing URL Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Koi bhi URL daalo aur check karo Safe hai ya Phishing</p>', unsafe_allow_html=True)

url = st.text_input("URL", "", label_visibility="collapsed", placeholder="https://example.com")

def check_url(url):
    if not url:
        return "EMPTY"
    
    if not url.startswith("http"):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '').lower()
    
    # SIRF YEHI SAFE
    trusted = ["google.com", "youtube.com", "facebook.com", "instagram.com", 
               "amazon.com", "github.com", "microsoft.com", "render.com"]
    
    if domain in trusted:
        return "SAFE"
    
    return "PHISHING"

if st.button("🚀 SCAN KARO"):
    result = check_url(url)
    
    if result == "EMPTY":
        st.warning("⚠️ Pehle URL daalo")
    elif result == "SAFE":
        st.success("✅ YE URL SAFE HAI")
    elif result == "PHISHING":
        st.error("⚠️ YE PHISHING URL HAI!")

st.markdown('</div>', unsafe_allow_html=True)
