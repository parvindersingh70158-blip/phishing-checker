
from flask import Flask, render_template, request
import whois
from datetime import datetime
import re

app = Flask(__name__)

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days
        return f"{age} days old"
    except:
        return "Could not fetch"

def check_phishing(url):
    issues = []
    safe = True
    
    # 1. Check for @ symbol
    if "@" in url:
        issues.append("URL contains @ symbol - used for phishing")
        safe = False
    
    # 2. Check for IP address instead of domain
    if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
        issues.append("URL uses IP address instead of domain name")
        safe = False
    
    # 3. Check for HTTPS
    if not url.startswith("https://"):
        issues.append("URL does not use HTTPS - not secure")
        safe = False
    
    # 4. Check for long URL
    if len(url) > 75:
        issues.append("URL is unusually long")
        safe = False
    
    return {"safe": safe, "issues": issues}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    url = ""
    domain_age = ""
    
    if request.method == "POST":
        url = request.form["url"]
        result = check_phishing(url)
        
        # Get domain from URL
        try:
            domain = url.split("//")[1].split("/")[0].split("@")[-1]
            domain_age = get_domain_age(domain)
        except:
            domain_age = "Invalid URL"
    
    return render_template("index.html", result=result, url=url, domain_age=domain_age)

if __name__ == "__main__":
    app.run(debug=True)