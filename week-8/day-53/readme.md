# obejctives

- automate a data entry task
- use selenium, beautifulsoup, and google forms to take property data from zillow that matches specified criteria
- put url, price, and name of listing into google form for each matching result
- scrape with beautifulsoup, fill google form with selenium

## steps taken

1. set up google form to act as place to enter each line of data scraped
2. went to [zillow](https://zillow.com) to build the specific query filters that i would like to use (toronto, 2+beds, townhouse/house, up to $2.5k per month 🥲) and saved url to use for requests
3. used `beautifulsoup` to scrape html from url with filters into a variable
4. added headers to attempt to bypass zillow captcha page
