#!/usr/bin/env python3
import json
import urllib.request
import urllib.error

API_KEY = "d00ed3ee747299f665b04f29cd0fab9c"
HOST = "about-us.sangyo-tech.jp"
ENDPOINT = "https://api.indexnow.org/indexnow"
URLS = [
    "https://about-us.sangyo-tech.jp/",
    "https://about-us.sangyo-tech.jp/llms/",
    "https://about-us.sangyo-tech.jp/sitemap.xml",
]

payload = {
    "host": HOST,
    "key": API_KEY,
    "keyLocation": f"https://{HOST}/{API_KEY}.txt",
    "urlList": URLS,
}
req = urllib.request.Request(
    ENDPOINT,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "User-Agent": "sangyo-tech-indexnow/1.0"},
)
try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        print(f"Status: {resp.status}")
        body = resp.read().decode("utf-8", errors="replace")
        if body:
            print(body)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} {e.reason}")
    print(e.read().decode("utf-8", errors="replace"))
