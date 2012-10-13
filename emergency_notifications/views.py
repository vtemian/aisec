import requests


MAILGUN_KEY = 'key-7kk2ob1dscvrdv2lwoklhbwjj8boaky6'

def send_email(to):
  return requests.post(
          "https://api.mailgun.net/v2/commkat.mailgun.org/messages",
          auth=("api", MAILGUN_KEY),
          data={"from": "COMMKAT <commkat@commkat.mailgun.org>",
                "to": [to],
                "subject": "Missing notification",
                "text": "Check your account...you have some important stuff to check!"}
  )


