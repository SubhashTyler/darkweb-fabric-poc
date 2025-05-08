import requests, hashlib, time, json
from bs4 import BeautifulSoup

session = requests.Session()
session.proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

url = 'http://someonionsite.onion'

try:
    res = session.get(url, timeout=30)
    content = BeautifulSoup(res.text, 'html.parser').get_text()
    hash_val = hashlib.sha256(content.encode()).hexdigest()

    log = {
        "id": str(int(time.time())),
        "hash": hash_val,
        "source": url,
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

    with open("scraped.json", "w") as f:
        json.dump(log, f, indent=2)
    print("Scraped and hashed successfully.")
except Exception as e:
    print("Error:", e)
