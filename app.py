from flask import Flask, render_template, request
import requests
import whois
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
    suspicious_words = ['login', 'verify', 'update', 'bank', 'paypal', 'account']
    for word in suspicious_words:
        if word in url.lower():
            issues.append(f"Suspicious keyword found: {word}")
    
    # 3. Check domain age using whois
    try:
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
            
        if creation_date:
            age_days = (datetime.now() - creation_date).days
            domain_age = f"{age_days} days old"
            if age_days < 90:
                issues.append(f"New domain - only {age_days} days old")
                safe = False
        else:
            domain_age = "Could not fetch"
    except:
        domain_age = "Could not fetch"
        issues.append("Could not verify domain info")
    
    return {'safe': safe, 'issues': issues, 'domain_age': domain_age}


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    url = None
    domain_age = None
    
    if request.method == 'POST':
        url = request.form['url']
        result_dict = check_url(url)
        
        # Yahi se JSON thik hoga
        if result_dict['safe']:
            result = "✅ SAFE - Ye website safe hai"
        else:
            result = "⚠️ SUSPICIOUS - " + ", ".join(result_dict['issues'])
            
        domain_age = result_dict['domain_age']

    return render_template('index.html', result=result, url=url, domain_age=domain_age)


if __name__ == '__main__':
    app.run(debug=True)
