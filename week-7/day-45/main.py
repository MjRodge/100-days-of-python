import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_html = response.text

movie_soup = BeautifulSoup(movie_html, "html.parser")
movie_names = movie_soup.find_all(name="h3")

print(movie_names)