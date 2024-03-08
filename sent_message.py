from twilio.rest import Client  # Import the necessary Twilio library

def send_message(body):
    account_sid = 'AC50c33e73eb286359d32ae1126c0f3336'
    auth_token = 'cce5d9ace8bf844c25eb02a1a1964bd0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to='919407575201',
        from_='12093065391',
        body=body
    )

    print(message.sid)

