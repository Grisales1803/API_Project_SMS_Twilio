import os
from twilio.rest import Client

def send_SMS(contact, msg):
    # My Twilio number
    my_twilio_number = '+14158013936'
    # Extract 'to' number:
    to_number = contact['Phone']
    # Extract the contact name
    contact_name = contact['Name']

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = msg,
        from_= my_twilio_number,
        to = to_number,
    )

    print(f'Message sent to {contact_name}.')