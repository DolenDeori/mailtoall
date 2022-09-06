from email.mime.text import MIMEText
import smtplib
import ssl
import pandas as pd
# GDSC_mails = pd.read_csv("GDSCML.csv")

smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

sender_email = "deepakdeori54@gmail.com"  # email address used to generate password

"""uncomment this when you have a csv file with a coloumn name "Email ID (personal)"""
# receiver_email = [mail for mail in GDSC_mails["Email ID (personal)"]

receiver_email = ["list of recipietns email"] # a list of recipients 
password = "" # the 16 code generated

# if you store credentials as env variables 
# password = os.environ['EMAIL_CRED']

from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["Subject"] = "YOur Subject"
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email) 

# reading the HTML file
html_file = open("index.html", "r")
read_html = html_file.read()

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