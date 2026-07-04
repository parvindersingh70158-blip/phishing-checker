from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

def check_url(url):
    issues = []
    safe = True
    
    if not url.startswith('https://'):
        issues.append("No HTTPS")
        safe = False
    
    if 'login' in url.lower() or 'verify' in url.lower():
        issues.append("Suspicious keywords")
        safe = False
    
    if len(url) > 75:
        issues.append("URL too long")
        safe = False
    
    domain_age = "N/A"
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
            result = "✅ SAFE"
        else:
            result = "⚠️ SUSPICIOUS: " + ", ".join(result_dict['issues'])
        domain_age = result_dict['domain_age']
    return render_template('index.html', result=result, url=url, domain_age=domain_age)

if __name__ == '__main__':
    app.run()
