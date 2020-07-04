#!/bin/bash/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''
Testing Failed.
'''

sender_address = 'ayushkumar.tiwari@gmail.com'
sender_pass = 'burningdesire'
receiver_address = 'ayushkumar.tiwari@gmail.com'

message = MIMEMultipart() 
message['From'] = sender_address 
message['To'] = receiver_address
message['Subject'] = 'Testing status'

message.attach(MIMEText(mail_content,'plain'))

session = smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
