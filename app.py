def check_url(url):
    url_lower = url.lower()
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    
    # 1. Trusted websites - direct SAFE
    trusted = [
        'google.com', 'facebook.com', 'youtube.com', 'amazon.com', 
        'github.com', 'microsoft.com', 'instagram.com', 'render.com',
        'netlify.com', 'vercel.com', 'stackoverflow.com'
    ]
    if domain in trusted: 
        return "SAFE"
    
    # 2. Check for phishing signs - score system
    score = 0
    if not url.startswith('https'): score += 3  # http hai to dangerous
    if '@' in url: score += 3
    if domain.count('.') > 3: score += 2  # bahut saare . hai
    if '-' in domain: score += 1
    if any(w in url_lower for w in ['login','verify','account','update','secure','bank','paypal','otp']): score += 2
    if 'bit.ly' in url_lower or 'tinyurl' in url_lower: score += 2
    
    # 3. Final decision
    if score >= 3:
        return "PHISHING"
    else:
        return "SAFE"  # normal websites SAFE
