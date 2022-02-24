from twilio.rest import Client
from keys import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TO_PHONE_NUMBER, FROM_PHONE_NUMBER

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.message = ""

    def send_text_notification(self, notification):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(body=notification, from_=FROM_PHONE_NUMBER, to=TO_PHONE_NUMBER)

