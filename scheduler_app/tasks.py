# tasks.py
from celery import Celery
from twilio.rest import Client
from config import BROKER_URL

celery = Celery(__name__, broker=BROKER_URL)


@celery.task
def send_whatsapp_message(phone_number, message):
    # Twilio setup
    account_sid = "copy from twilio"
    auth_token = "copy from twilio"
    client = Client(account_sid, auth_token)

    # Send WhatsApp message using Twilio API
    message = client.messages.create(
        body=message,
        from_="whatsapp:+14155238886",  # Twilio's WhatsApp sandbox number
        to=f"whatsapp:+{phone_number}",
    )
    print(f"Message sent: {message.sid}")
