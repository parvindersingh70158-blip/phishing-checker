import streamlit as st
import pickle
import numpy as np
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="centered")
st.title("🔒 Phishing URL Checker")
st.write("Enter any URL to check if it is Safe or Phishing")

@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

def extract_features(url):
    features = []
    parsed = urlparse(url)
    domain = parsed.netloc
    url_lower = url.lower()
    
    # EXACT 30 FEATURES - MUST MATCH TRAINING
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('&'))
    features.append(url.count('='))
    features.append(url.count('_'))
    features.append(url.count('%'))
    features.append(1 if 'https' in url else 0)
    features.append(1 if 'http' in url else 0)
    features.append(len(domain))
    features.append(len(parsed.path))
    features.append(url.count('www'))
    features.append(1 if domain.count('.') > 3 else 0)
    features.append(1 if 'bit.ly' in url_lower else 0)
    features.append(1 if 'tinyurl' in url_lower else 0)
    features.append(1 if 'login' in url_lower else 0)
    features.append(1 if 'secure' in url_lower else 0)
    features.append(1 if 'account' in url_lower else 0)
    features.append(1 if 'update' in url_lower else 0)
    features.append(1 if 'verify' in url_lower else 0)
    features.append(1 if 'bank' in url_lower else 0)
    features.append(1 if 'paypal' in url_lower else 0)
    features.append(1 if 'amazon' in url_lower else 0)
    features.append(1 if 'google' in url_lower else 0)
    features.append(1 if 'facebook' in url_lower else 0)
    features.append(1 if 'twitter' in url_lower else 0)
    features.append(1 if 'instagram' in url_lower else 0)
    
    return np.array([features])

url = st.text_input("Enter URL here:", "https://google.com")

if st.button("Check URL"):
    if url:
        features = extract_features(url)
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ THIS IS A PHISHING URL!")
            st.write("Do not click on this link")
        else:
            st.success("✅ THIS URL IS SAFE")
            st.write("You can proceed")
    else:
        st.warning("Please enter a URL first")
