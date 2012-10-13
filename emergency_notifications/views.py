import requests


def send_email():
  return requests.post(
          "https://api.mailgun.net/v2/samples.mailgun.org/messages",
          auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
          data={"from": "Excited User <me@samples.mailgun.org>",
                "to": ["sergeyo@profista.com", "serobnic@mail.ru"],
                "subject": "Hello",
                "text": "Testing some Mailgun awesomness!"}
  )
