def check_url(url):
    if not url:
        return "ERROR"
    
    url_lower = url.lower()
    
    # agar https nahi hai to jod de warna domain nahi milega
    if not url.startswith('http'):
        url = 'https://' + url
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').lower()
    except:
        domain = url.replace('www.', '').replace('https://','').replace('http://','').lower()
    
    # Trusted list - ab render bhi hai
    trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'render.com', 'netlify.com', 'microsoft.com']
    if domain in trusted: 
        return "SAFE"
    
    # Phishing checks
    score = 0
    if not url.startswith('https'): score += 3
    if '@' in url: score += 3
    if domain.count('.') > 3: score += 2
    if '-' in domain: score += 1
    if any(w in url_lower for w in ['login','verify','account','update','bank','paypal','otp']): score += 2
    
    if score >= 3:
        return "PHISHING"
    else:
        return "SAFE"
