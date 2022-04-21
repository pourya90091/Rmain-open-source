from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(sender, getter, password, subject, message):
    print(f"sender : {sender}\ngetter : {getter}")
    smtp_server = "smtp.gmail.com:587"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = getter
    msg['Subject'] = subject

    message = message
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server)
        server.starttls()
        server.login(msg["From"], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print(f"email sent from {sender} to {getter}")
    except Exception as err:
        raise Exception(err)
