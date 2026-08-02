import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="centered")
st.title("🔒 Phishing URL Checker")
st.write("Enter any URL to check if it is Safe or Phishing")

def check_url(url):
    url_lower = url.lower()
    
    # Trusted websites - direct SAFE
    trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'microsoft.com']
    if any(t in url_lower for t in trusted):
        return "SAFE"
    
    score = 0
    # Red flags
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

if st.button("Check URL"):
    if url:
        result = check_url(url)
        
        if result == "PHISHING":
            st.error("⚠️ THIS IS A PHISHING URL!")
            st.write("Do not click on this link")
        else:
            st.success("✅ THIS URL IS SAFE")
            st.write("You can proceed safely")
    else:
        st.warning("Please enter a URL first")
