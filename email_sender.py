import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Cathy'
email['to'] = 'Min'
email['subject'] = 'Test and test'

email.set_content("Hello, this is me speaking")
print(email)
