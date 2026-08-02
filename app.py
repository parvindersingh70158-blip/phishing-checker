import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="centered")
st.title("🔒 Phishing URL Checker")
st.write("Enter any URL to check if it is Safe or Phishing")

def check_url(url):
    url_lower = url.lower()
    suspicious_words = ['login', 'verify', 'account', 'update', 'secure', 'bank', 'paypal']
    suspicious_domains = ['bit.ly', 'tinyurl']
    
    score = 0
    if 'https' not in url: score += 2
    if '@' in url: score += 3
    if url.count('.') > 3: score += 2
    if any(word in url_lower for word in suspicious_words): score += 2
    if any(d in url_lower for d in suspicious_domains): score += 3
    
    if score >= 4:
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
            st.write("You can proceed")
    else:
        st.warning("Please enter a URL first")
