from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_title = soup.find(name="a", class_="storylink")
print(article_title)

# with open("website.html") as website:
#     website_content = website.read()
#     # print(website_content)
#
# soup = BeautifulSoup(website_content, "html.parser")
# print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
