import smtplib
import pandas
import datetime as dt
from secrets import my_email, my_password


# configure smtp connection with gmail account
def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        # my_email my_password configured in secrets.py
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="michael@1mrkt.to", msg=f"Subject:python quote\n\nauthor: {author}, message: {quote_text}")


# load quotes from csv
quotes = pandas.read_csv("quotes.csv")
# find a single random quote using pandas sample() function
random_quote = quotes.sample()
# assign the author and quote text to variables
author = random_quote["Author"].loc[random_quote.index[0]]
quote_text = random_quote["Quote"].loc[random_quote.index[0]]

now = dt.datetime.now()
weekday = now.weekday()

# send message on Monday (weekday == 0)
if weekday == 0:
    send_mail()
