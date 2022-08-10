import logging
import smtplib
from email.mime.text import MIMEText

sendable_email_address = ""

def send(message_body="", is_error=False):
    assert sendable_email_address != ""

    body = str(message_body)
    body += '\n\n(automatically sent by process-watchdog)'
    msg = MIMEText(body)
    msg['Subject'] = "Process Errored" if is_error else "Process Complete"
    # From is required
    msg['From'] = 'watchdog@localhost'
    msg['To'] = sendable_email_address


    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    try:
        s.send_message(msg)
    finally:
        s.quit()
