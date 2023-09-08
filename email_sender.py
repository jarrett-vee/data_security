# This program is an extension of the Weed Maps Scraper (find that on my account) and uses the data pulled for an email bombing campaign.
# Very simple script that sends an email to a list of targets.

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# email info, proof of concept using outlook.
smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_username = "email@outlook.com"
smtp_password = "email_password"


def send_email(to_name, to_email):
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = to_email
    msg["Subject"] = "Question"

    body = f"""Hi {to_name}, I recently visited your store and my product appeared expired. I found this on it, is this mold? https://imgur.com/gallery/malware_example_not_actually_real"""

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        email = row[1]
        send_email(name, email)
print("Emails sent.")
