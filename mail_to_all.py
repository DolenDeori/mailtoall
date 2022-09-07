from email.mime.text import MIMEText
import os
import sys
import smtplib
import ssl
import pandas as pd
from email.mime.multipart import MIMEMultipart
from config import *

smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

print("Trying to connect...")
try:
    if os.path.exists("mails.csv"):
        gdsc_mails = pd.read_csv("mails.csv")
        receiver_email = [mail for mail in gdsc_mails["Email ID (personal)"]] #this will only work when you have a csv file with a coloumn name "Email ID (personal)
    else:
        receiver_email = target_users
except:
    print("\nWe need receiver emails!")
    sys.exit()

msg = MIMEMultipart()
msg["Subject"] = mail_subject
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email) 

# reading the HTML file
try:
    html_file = open("index.html", "r")
    read_html = html_file.read()
except FileNotFoundError:
    print("\nmail(index.html) not found!")
    sys.exit()

# Making an HTML object to send with the email
html = f"{read_html}"

body_html = MIMEText(html, 'html')  # parse values into html text
msg.attach(body_html)

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # check connection
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # check connection
    server.login(sender_email, password)

    # Send email here
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("message sent successfuly !!!")

except Exception as e:
    # Print any error messages 
    print(e)
finally:
    server.quit()