# Інтерфейс програмування
# 1. Написати програму, яка буде робити запит на один із 5 сайтів і друкувати статус-код відповіді, назву сайту,
# а також довжину HTML-коду із відповіді.
# Вибір сайту для здійснення запиту має бути здійснений випадковим чином (random).

import requests
import random

sites = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "amazon.com",
    "apple.com",
]

site = "https://" + random.choice(sites)
res = requests.get(site)

print(f"site: {site}")
print(res.status_code)
print(f"HTML length: {len(res.text)}")