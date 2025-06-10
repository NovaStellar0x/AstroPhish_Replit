import requests

def fetch_phishtank_urls():
    url = "https://data.phishtank.com/data/online-valid.json"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        return [entry['url'] for entry in data]
    except Exception as e:
        print(f"[!] Error fetching PhishTank: {e}")
        return []