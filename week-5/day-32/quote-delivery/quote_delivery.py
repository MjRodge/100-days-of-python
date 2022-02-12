import smtplib
from secrets import my_email, my_password

# configure smtp connection with gmail account
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    # my_email my_password configured in secrets.py
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="michael@1mrkt.to", msg="Subject:third testing from python\n\nThis is the body of the email, i hope it works!")

with open("quotes.csv", "r") as quote_contents:
    quotes = quote_contents.readlines()

print(quotes)