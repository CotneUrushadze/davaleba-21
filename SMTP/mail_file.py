import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtp_host = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'cotneishot@gmail.com'
password = getpass("Enter your app password: ")  

receiver_email = 'nika@mziuri.ge'
file_path = r'C:\Users\ILOo\Desktop\a.txt'

message = MIMEMultipart()
message['Subject'] = 'სატესტო - Attached File'
message['From'] = sender_email
message['To'] = receiver_email
text = MIMEText('ფაილი')
message.attach(text)

try:
    with open(file_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), Name=file_path)
        attachment['Content-Disposition'] = f'attachment; filename="{file_path}"'
        message.attach(attachment)
except FileNotFoundError:
    print("file not found")

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
print("email sent successfully")

