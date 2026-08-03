def check_url(url):
    if not url:
        return "EMPTY"
    
    if not url.startswith("http"):
        url = "https://" + url
    
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '').lower()
    
    # 1. SIRF YEHI SAFE HAI - iske alawa sab PHISHING
    trusted = [
        "google.com", "youtube.com", "facebook.com", "instagram.com", 
        "amazon.com", "github.com", "microsoft.com", "twitter.com",
        "linkedin.com", "netflix.com", "render.com"
    ]
    
    if domain in trusted:
        return "SAFE"
    
    # 2. BAAT SAB PHISHING
    return "PHISHING"
