import streamlit as st
from urllib.parse import urlparse
import streamlit.components.v1 as components

st.set_page_config(page_title="Phishing URL Checker", layout="wide")

# ANIMATED PARTICLE BACKGROUND
components.html("""
<style>
body {margin: 0; overflow: hidden;}
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

# CLEAN UI CSS
st.markdown("""
<style>
    #MainMenu, footer {visibility: hidden;}
    .stApp {background: transparent;}
    
    .main-box {
        background: rgba(15, 20, 35, 0.85);
        backdrop-filter: blur(5px);
        padding: 40px;
        border-radius: 15px;
        max-width: 700px;
        margin: 60px auto;
        text-align: center;
    }
    
    /* Title inside box with glow */
    .title-box {
        background: rgba(0, 114, 255, 0.2);
        border: 1px solid #00c6ff;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 25px;
    }
    .title-box h1 {
        color: #00e5ff !important;
        text-shadow: 0 0 10px #00e5ff;
        margin: 0;
    }
    
    /* Smaller input box */
    .stTextInput {
        max-width: 500px;
        margin: 0 auto;
    }
    .stTextInput>div>div>input {
        background: rgba(0,0,0,0.5);
        color: white;
        border: 1px solid #0072ff;
        border-radius: 8px;
        text-align: center;
    }
    
    /* Center button */
    div.stButton {text-align: center;}
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 35px;
        font-weight: bold;
        font-size: 16px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)

# TITLE IN BOX
st.markdown('<div class="title-box"><h1>🔒 Phishing URL Checker</h1></div>', unsafe_allow_html=True)

st.write("Enter any URL to verify if it is **Safe** or **Phishing**")

url = st.text_input("", "https://google.com", label_visibility="collapsed")

if st.button("🚀 SCAN URL NOW"):
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
