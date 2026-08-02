def check_url(url):
    url_lower = url.lower()
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    
    # Only these 7 are SAFE
    trusted = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'github.com', 'microsoft.com', 'instagram.com']
    
    if domain in trusted: 
        return "SAFE"
    
    # Everything else is PHISHING for demo
    return "PHISHING"
