from bs4 import BeautifulSoup

with open("website.html") as website:
    website_content = website.read()
    # print(website_content)

soup = BeautifulSoup(website_content, "html.parser")
print(soup.prettify())
