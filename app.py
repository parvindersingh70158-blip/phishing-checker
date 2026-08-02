import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker")

st.title("🔒 Phishing URL Checker")
st.write("Enter any URL to verify if it is **Safe** or **Phishing**")

url = st.text_input("Enter URL", "https://google.com")

def check_url(url):
    if not url:
        return "ERROR"
    
    url_lower = url.lower()
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '')
    except:
        domain = url.replace('www.', '')
    
    # Trusted list
    trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'render.com']
    if domain in trusted: 
        return "SAFE"
    
    # Phishing checks
    score = 0
    if not url.startswith('https'): score += 3
    if '@' in url: score += 3
    if domain.count('.') > 3: score += 2
    if '-' in domain: score += 1
    if any(w in url_lower for w in ['login','verify','account','update','bank','paypal']): score += 2
    
    if score >= 3:
        return "PHISHING"
    else:
        return "SAFE"

if st.button("SCAN URL NOW"):
    result = check_url(url)
    
    if result == "PHISHING":
        st.error("⚠️ THIS IS A PHISHING URL!")
    elif result == "SAFE":
        st.success("✅ THIS URL IS SAFE")
    else:
        st.warning("Please enter a valid URL")
