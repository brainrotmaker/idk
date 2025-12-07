# proxy_mgr.py – Free elite rotation (low ban rate)
import random
import logging

logger = logging.getLogger(__name__)

# Load proxies from file
proxies = []

def load_proxies():
    global proxies
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"Loaded {len(proxies)} free elite proxies")
    except:
        print("proxies.txt missing – using no proxy (slower)")

def get_proxy():
    if not proxies:
        return None
    return random.choice(proxies)
