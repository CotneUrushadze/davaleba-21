import smtplib
from getpass import getpass
from email.mime.text import MIMEText

smtp_host = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'cotneishot@gmail.com'
password = getpass('Enter your email password: ')

receiver_email = 'nika@mziuri.ge'
message  = MIMEText('Lorem ipsum dolor sit amet')
message ['Subject'] = 'სატესტო'
message ['From'] = sender_email
message ['To'] = receiver_email

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("email sent successfully")