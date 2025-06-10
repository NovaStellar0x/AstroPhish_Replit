import requests

def fetch_openphish_urls():
    url = "https://openphish.com/feed.txt"
    try:
        r = requests.get(url, timeout=10)
        return r.text.strip().split('\n')
    except Exception as e:
        print(f"[!] Error fetching OpenPhish: {e}")
        return []