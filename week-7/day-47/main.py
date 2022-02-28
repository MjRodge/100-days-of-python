import requests
from bs4 import BeautifulSoup
import smtplib
from keys import FROM_ADDR, TO_ADDR, EMAIL_PASSWORD

AMAZON_URL = "https://www.amazon.ca/Apple-MacBook-14-inch-8‑core-14‑core/dp/B09JQSLL92/ref=sr_1_1"

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98."
}
# set the lowest price for the user to be emailed a notification
PRICE_THRESHOLD = 2600

# get the data from amazon url
response = requests.get(url=AMAZON_URL, headers=HEADERS)
amazon_html = response.text
amazon_soup = BeautifulSoup(amazon_html, "html.parser")
# pull out dollar/cent value of item and combine into a variable, stripping unnecessary characters
dollars = amazon_soup.find(name="span", class_="a-price-whole").get_text().replace(",", "")
cents = amazon_soup.find(name="span", class_="a-price-fraction").get_text()
price = float(f"{dollars}{cents}")

product_title = amazon_soup.find(name="span", id="productTitle").get_text()

message = f"Subject: Amazon Price Alert\n\n{product_title} is on sale!\nPurchase here: {AMAZON_URL}"
print(message)

# email_connection = smtplib.SMTP("smtp.gmail.com", 587)
# email_connection.starttls()
# email_connection.login(user=FROM_ADDR, password=EMAIL_PASSWORD)
# email_connection.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=message)

print(type(price))
