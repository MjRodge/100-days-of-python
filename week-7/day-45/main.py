from bs4 import BeautifulSoup

with open("website.html") as website:
    website_content = website.read()
    # print(website_content)

soup = BeautifulSoup(website_content, "html.parser")
print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.get("href"))

company_url = soup.select_one(selector="p a")
print(company_url)
