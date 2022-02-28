import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

target_date = input("please enter a date in format yyyy-mm-dd that you would like to search for: ")

response = requests.get(f"{BILLBOARD_URL}/{target_date}")
chart_html = response.text

chart_soup = BeautifulSoup(chart_html, "html.parser")
print(chart_soup)
