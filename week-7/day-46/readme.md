# day 46 - billboard 100 spotify playlist

## objectives 
- create a program that takes an input of a date from the user
- use this data to search the [billboard 100](https://www.billboard.com/charts/hot-100/2000-08-12/) website for the top 100 chart hits on the provided date, and use beautiful soup to scrape song titles
- authorise with the spotify api, and use the song titles scraped to build a playlist

## apis used
- [list here]

## steps taken
1. take a date in format yyyy-mm-dd from the user, and save to a variable
2. use `beautifulsoup` to scrape the html of the billboard 100 website for the desired date
3. use class selectors to grab the song title text from the scraped html
4. use list comprehension to strip all html characters and store only song title text in a list
5. select and append the number 1 song of the week, as this was not selected by the class selector for other 99 songs
6. log into the [spotify developer portal](https://developer.spotify.com/dashboard/applications) and create a new application
7. create `keys.py` and `.gitignore` to save spotify api tokens