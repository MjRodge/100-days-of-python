import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

target_date = input("please enter a date in format yyyy-mm-dd that you would like to search for: ")

response = requests.get(f"{BILLBOARD_URL}/{target_date}")
chart_html = response.text

chart_soup = BeautifulSoup(chart_html, "html.parser")
song_titles = chart_soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
print(song_titles)
