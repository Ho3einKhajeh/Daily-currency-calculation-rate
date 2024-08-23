import smtplib
import requests

from config import EMAIL_RECIVER, rules
from email.mime.text import MIMEText


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = ""
    msg['To'] = rules['email']['reciver']

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('', '')
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())

