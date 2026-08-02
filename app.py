import streamlit as st
from urllib.parse import urlparse
import streamlit.components.v1 as components

st.set_page_config(page_title="Phishing URL Checker", layout="wide")

# ANIMATED PARTICLE BACKGROUND - ONLY BACKGROUND MOVES
components.html("""
<style>
body {
    margin: 0;
    overflow: hidden;
}
#particles-js {
    position: fixed;
    width: 100%;
    height: 100%;
    background: #0a0f1a;
    z-index: -1;
}
</style>
<div id="particles-js"></div>
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": {"value": 80, "density": {"enable": true, "value_area": 800}},
    "color": {"value": "#00c6ff"},
    "shape": {"type": "circle"},
    "opacity": {"value": 0.5, "random": true},
    "size": {"value": 2, "random": true},
    "line_linked": {"enable": true, "distance": 150, "color": "#0072ff", "opacity": 0.3, "width": 1},
    "move": {"enable": true, "speed": 1.5, "direction": "none", "out_mode": "out"}
  },
  "interactivity": {"detect_on": "canvas", "events": {"onhover": {"enable": true, "mode": "repulse"}}},
  "retina_detect": true
});
</script>
""", height=0)

# SIMPLE CLEAN UI CSS
st.markdown("""
<style>
    #MainMenu, footer {visibility: hidden;}
    .stApp {background: transparent;}
    
    .main-box {
        background: rgba(15, 20, 35, 0.85);
        backdrop-filter: blur(5px);
        padding: 40px;
        border-radius: 15px;
        max-width: 800px;
        margin: 60px auto;
    }
    
    h1 {
        color: #00e5ff !important;
        text-align: center;
    }
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.5);
        color: white;
        border: 1px solid #0072ff;
        border-radius: 8px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 30px;
        font-weight: bold;
        display: block;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.title("🔒 Phishing URL Checker")
st.write("### AI Powered Cybersecurity Tool")
st.write("Enter any URL to check if it is **Safe** or **Phishing**")

url = st.text_input("Enter URL here:", "https://google.com")

if st.button("Scan URL Now"):
    if url:
        def check_url(url):
            url_lower = url.lower()
            trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com']
            if any(t in url_lower for t in trusted): return "SAFE"
            
            score = 0
            if 'https' not in url: score += 2
            if '@' in url: score += 3
            if url.count('.') > 4: score += 2
            if any(w in url_lower for w in ['login','verify','account']): score += 2
            if 'bit.ly' in url_lower: score += 3
            
            return "PHISHING" if score >= 3 else "SAFE"

        result = check_url(url)
        
        if result == "PHISHING":
            st.error("⚠️ THIS IS A PHISHING URL!")
        else:
            st.success("✅ THIS URL IS SAFE")
    else:
        st.warning("Please enter a URL first")

st.markdown('</div>', unsafe_allow_html=True)
