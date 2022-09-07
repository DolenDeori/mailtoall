from email.mime.text import MIMEText
from operator import imod
import os
import sys
import smtplib
import ssl
import pandas as pd
from email.mime.multipart import MIMEMultipart
from config_data import *

smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

if __name__ == "__main__":
    file_path = get_csv()
    try:
        if os.path.exists(file_path):
            gdsc_mails = pd.read_csv(file_path)
            receiver_email = [mail for mail in gdsc_mails["email"]] #this will only work when you have a csv file with a coloumn name "Email ID (personal)
            msg = MIMEMultipart()
            msg["Subject"] = mail_subject
            msg["From"] = sender_email
            msg['To'] = ", ".join(receiver_email)
        else:
            print("CSV File Not Found :(")
    except:
        print("\nWe need receiver emails!")
        sys.exit()

    # reading the HTML file
    try:
        # html_file = open("index.html", "r")
        # read_html = html_file.read()

        with open("index.html", "r") as f:
            read_html = f.read()
    except FileNotFoundError:
        print("mail(index.html) not found!")
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