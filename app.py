import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker")

st.title("🔒 Phishing URL Checker")
st.write("Enter any URL and click SCAN")

url = st.text_input("URL", "")

def check_url(url):
    if not url:
        return "EMPTY"
    
    # https add karna hai to add kar de
    if not url.startswith("http"):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '').lower()
    
    # SAFE LIST
    trusted = ["google.com", "youtube.com", "facebook.com", "amazon.com", "github.com", "microsoft.com", "render.com", "netlify.com"]
    
    if domain in trusted:
        return "SAFE"
    
    # PHISHING CHECKS
    score = 0
    if "https" not in url: score += 3
    if "@" in url: score += 3
    if "-" in domain: score += 1
    if domain.count(".") > 3: score += 2
    if any(x in url.lower() for x in ["login","verify","account","bank","paypal","otp"]): score += 2
    
    if score >= 3:
        return "PHISHING"
    return "SAFE"

if st.button("SCAN URL NOW"):
    result = check_url(url)
    
    if result == "EMPTY":
        st.warning("Please enter a URL")
    elif result == "SAFE":
        st.success("✅ THIS URL IS SAFE")
    elif result == "PHISHING":
        st.error("⚠️ THIS IS A PHISHING URL!")
