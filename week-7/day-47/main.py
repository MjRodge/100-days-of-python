import requests
from bs4 import BeautifulSoup

AMAZON_URL = "https://www.amazon.ca/Apple-MacBook-14-inch-8‑core-14‑core/dp/B09JQSLL92/ref=sr_1_1"

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98."
}

response = requests.get(url=AMAZON_URL, headers=HEADERS)
amazon_html = response.text
amazon_soup = BeautifulSoup(amazon_html, "html.parser")
dollars = amazon_soup.find(name="span", class_="a-price-whole").get_text().replace(",", "")
cents = amazon_soup.find(name="span", class_="a-price-fraction").get_text()
price = float(f"{dollars}{cents}")

print(type(price))
