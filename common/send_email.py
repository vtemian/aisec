#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#
#def prepare_message(toEmail, fromEmail, subjectEmail):
#    msg = MIMEMultipart('alternative')
#    msg['Subject'] = subjectEmail
#    msg['From'] = fromEmail
#    msg['To'] = toEmail
#
#    return msg
#
#def send_email(msg):
#    # Login credentials
#    username = 'vtemian'
#    password = "seleus00"
#
#    # Open a connection to the SendGrid mail server
#    s = smtplib.SMTP('smtp.sendgrid.net', 587)
#
#        # Attach parts into message container.
#        msg.attach(part1)
#        msg.attach(part2)
#    # Authenticate
#    s.login(username, password)
#
#    # sendmail function takes 3 arguments: sender's address, recipient's address
#    # and message to send - here it is sent as one string.
#    s.sendmail(fromEmail, toEmail, msg.as_string())
#
#    s.quit()
#def create_email_body(text, html):
#    # Record the MIME types of both parts - text/plain and text/html.
#    part1 = MIMEText(text, 'plain')
#    part2 = MIMEText(html, 'html')
#
#    return part1, part2