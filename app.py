import streamlit as st
import pickle
import pandas as pd
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing URL Checker", layout="centered")
st.title("🔒 Phishing URL Checker")
st.write("Koi bhi URL daalo aur check karo ki wo Safe hai ya Phishing hai")

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
    
    # 30 features - same order me
    features.append(len(url)) #1
    features.append(url.count('.')) #2
    features.append(url.count('/')) #3
    features.append(url.count('-')) #4
    features.append(url.count('@')) #5
    features.append(url.count('?')) #6
    features.append(url.count('&')) #7
    features.append(url.count('=')) #8
    features.append(url.count('_')) #9
    features.append(url.count('%')) #10
    features.append(1 if 'https' in url else 0) #11
    features.append(1 if 'http' in url else 0) #12
    features.append(len(domain)) #13
    features.append(len(parsed.path)) #14
    features.append(url.count('www')) #15
    features.append(1 if domain.count('.') > 3 else 0) #16
    features.append(1 if 'bit.ly' in url else 0) #17
    features.append(1 if 'tinyurl' in url else 0) #18
    features.append(1 if 'login' in url.lower() else 0) #19
    features.append(1 if 'secure' in url.lower() else 0) #20
    features.append(1 if 'account' in url.lower() else 0) #21
    features.append(1 if 'update' in url.lower() else 0) #22
    features.append(1 if 'verify' in url.lower() else 0) #23
    features.append(1 if 'bank' in url.lower() else 0) #24
    features.append(1 if 'paypal' in url.lower() else 0) #25
    features.append(1 if 'amazon' in url.lower() else 0) #26
    features.append(1 if 'google' in url.lower() else 0) #27
    features.append(1 if 'facebook' in url.lower() else 0) #28
    features.append(1 if 'twitter' in url.lower() else 0) #29
    features.append(1 if 'instagram' in url.lower() else 0) #30
    
    return [features]

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
