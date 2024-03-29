import requests
from twilio.rest import Client
from keys import STOCK_API, NEWS_API, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER, TO_PHONE_NUMBER

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "apikey": STOCK_API,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])
print(day_before_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
day_change = abs(yesterday_closing_price - day_before_closing_price)
print(day_change)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = day_change / ((yesterday_closing_price + day_before_closing_price) / 2) * 100
print(percentage_difference)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_params = {
    "q": STOCK_NAME,
    "apiKey": NEWS_API,
    "pageSize": 3  # limit response to three articles
}
if percentage_difference > 0:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"]
    print("get news")
    print(news_articles)
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
article_content = [f"headline: {article['title']}\n-- brief: {article['description']}" for article in news_articles]
print(article_content)

# TODO 9. - Send each article as a separate message via Twilio.
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

for article in article_content:
    message = client.messages \
        .create(
        body=article,
        from_=FROM_PHONE_NUMBER,
        to=TO_PHONE_NUMBER
    )

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
