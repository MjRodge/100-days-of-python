import smtplib

my_email = "test@email.com"
my_password = "abcd1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="destination@email.com",
        msg="Subject:Test Email\n\nThis is the email body."
    )