import streamlit as st
import pickle
import pandas as pd
import re
from urllib.parse import urlparse

# Page setting
st.set_page_config(page_title="Phishing URL Checker", layout="centered")

st.title("🔒 Phishing URL Checker")
st.write("Koi bhi URL daalo aur check karo ki wo Safe hai ya Phishing hai")

# Model load karo
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Simple feature nikalne wala function - agar tere model me aur feature hain to ye badalna padega
def extract_features(url):
    features = []
    features.append(len(url)) # length
    features.append(url.count('.')) # dots
    features.append(url.count('/')) # slashes
    features.append(1 if 'https' in url else 0) # https hai ya nahi
    features.append(1 if '@' in url else 0) # @ hai ya nahi
    features.append(1 if '-' in url else 0) # - hai ya nahi
    return [features]

# Input box
url = st.text_input("URL yaha daalo:", "https://google.com")

if st.button("Check Karo"):
    if url:
        features = extract_features(url)
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ YE PHISHING URL HAI!")
            st.write("Is link pe click mat karna")
        else:
            st.success("✅ YE SAFE URL HAI")
            st.write("Tension mat lo")
    else:
        st.warning("Pehle URL daalo bhai")

st.markdown("---")
st.caption("Made with Streamlit + ML")
