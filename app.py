from flask import Flask, render_template, request
import requests
from datetime import datetime
import re
from urllib.parse import urlparse

app = Flask(__name__)

def check_url(url):
    issues = []
    safe = True
    
    # 1. Check if URL has https
    if not url.startswith('https://'):
        issues.append("Website does not use HTTPS")
        safe = False
    
    # 2. Check for suspicious keywords
    suspicious_words = ['login', 'verify', 'update', 'bank', 'paypal', 'account', 'secure']
    for word in suspicious_words:
        if word in url.lower():
            issues.append(f"Suspicious keyword found: {word}")
            safe = False
    
    # 3. Check URL length - phishing urls are usually long
    if len(url) > 75:
        issues.append("URL is too long")
        safe = False
    
    domain_age = "Manual Check Needed" # whois hata diya isliye
    
    return {'safe': safe, 'issues': issues, 'domain_age': domain_age}


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    url = None
    domain_age = None
    
    if request.method == 'POST':
        url = request.form['url']
        result_dict = check_url(url)
        
        if result_dict['safe']:
            result = "✅ SAFE - Ye website safe lag rahi hai"
        else:
            result = "⚠️ SUSPICIOUS - " + ", ".join(result_dict['issues'])
            
        domain_age = result_dict['domain_age']

    return render_template('index.html', result=result, url=url, domain_age=domain_age)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
