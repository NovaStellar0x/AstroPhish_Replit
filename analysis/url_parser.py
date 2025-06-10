from urllib.parse import urlparse

def extract_url_info(url):
    try:
        parsed = urlparse(url)
        return {
            'url': url,
            'scheme': parsed.scheme,
            'domain': parsed.netloc,
            'path': parsed.path
        }
    except:
        return {'url': url, 'domain': 'parse_error'}