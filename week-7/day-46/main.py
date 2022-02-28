import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

target_date = input("please enter a date in format yyyy-mm-dd that you would like to search for: ")

response = requests.get(f"{BILLBOARD_URL}/{target_date}")
chart_html = response.text

# scrape all html from billboard website for user inputted date
chart_soup = BeautifulSoup(chart_html, "html.parser")
# find all of the h3 tags with relevant classes for song titles
song_titles = chart_soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# strip unwanted newline characters
song_title_text = [text.get_text().strip("\n") for text in song_titles]
# find and append the number 1 song as it has differing class names
no1_song = chart_soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").get_text().strip("\n")
song_title_text.insert(0, no1_song)


spotify_conn = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        scope="playlist-modify-private",
        redirect_uri="http://localhost",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotify_conn.current_user()["id"]
print(user_id)

