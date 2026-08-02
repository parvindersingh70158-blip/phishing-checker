from flask import Flask, render_template, request
import pickle
from urllib.parse import urlparse
import re

app = Flask(__name__)

# model load kar
model = pickle.load(open('model.pkl', 'rb'))

def extract_features(url):
    features = []
    parsed = urlparse(url)
    domain = parsed.netloc
    protocol = parsed.scheme

    # 1. having_IP_Address
    features.append(1 if re.match(r'^\d+\.\d+\.\d+\.\d+', domain) else 0)

    # 2. URL_Length
    if len(url) < 54: features.append(0)
    elif len(url) <= 75: features.append(1)
    else: features.append(1)

    # 3. Shortening_Service
    features.append(1 if re.search('bit\.ly|goo\.gl|tinyurl|t\.co|ow\.ly|tiny.cc', url) else 0)

    # 4. having_@_Symbol
    features.append(1 if '@' in url else 0)

    # 5. double_slash_redirecting
    features.append(1 if url.rfind('//') > 6 else 0)

    # 6. Prefix_Suffix - paypal-login.com
    features.append(1 if '-' in domain else 0)

    # 7. having_Sub_Domain
    if domain.count('.') == 1: features.append(0)
    elif domain.count('.') == 2: features.append(1)
    else: features.append(1)

    # 8. HTTPS - akela https se SAFE nahi
    features.append(1 if protocol == 'https' else 0)

    # 9. Domain_Registration_Length - dummy
    features.append(0)

    # 10. Favicon
    features.append(0)

    # 11. Port
    features.append(1 if ':' in domain else 0)

    # 12. HTTPS_Token - https domain ke beech me
    features.append(1 if 'https' in domain else 0)

    # 13. Request_URL
    features.append(0)

    # 14. URL_of_Anchor
    features.append(0)

    # 15. Links_in_tags
    features.append(0)

    # 16. SFH
    features.append(0)

    # 17. Submitting_to_email
    features.append(0)

    # 18. Abnormal_URL
    features.append(0)

    # 19. Redirect
    features.append(0)

    # 20. on_mouseover
    features.append(0)

    # 21. RightClick
    features.append(0)

    # 22. popUpWindow
    features.append(0)

    # 23. Iframe
    features.append(0)

    # 24. age_of_domain
    features.append(0)

    # 25. DNSRecord
    features.append(0)

    # 26. web_traffic
    features.append(0)

    # 27. Page_Rank
    features.append(0)

    # 28. Google_Index
    features.append(0)

    # 29. Links_pointing_to_page
    features.append(0)

    # 30. Statistical_report
    features.append(0)

    return [features]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    color = ""
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "SAFE ✅"
            color = "green"
        else:
            result = "DANGEROUS ❌"
            color = "red"

    return render_template('index.html', result=result, color=color)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)
