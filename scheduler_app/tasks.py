# tasks.py
from celery import Celery
from twilio.rest import Client
from config import BROKER_URL

celery = Celery(__name__, broker=BROKER_URL)

@celery.task
def send_whatsapp_message(phone_number, message):
    # Twilio setup
    account_sid = 'AC78755a0442669a4f318d28168f286ae2'
    auth_token = 'a471382acde06b192f4ecc0b35106d10'
    client = Client(account_sid, auth_token)

    # Send WhatsApp message using Twilio API
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Twilio's WhatsApp sandbox number
        to=f'whatsapp:+{phone_number}'
    )
    print(f"Message sent: {message.sid}")
