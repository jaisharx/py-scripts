import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('mail-body.html').read_text())
email = EmailMessage()
email['from'] = 'Jai Sharma'
email['to'] = 'sendtojsharma@gmail.com'
email['subject'] = 'Hi, there. We\'re sending this mail vai pythonscript.'

email.set_content(html.substitute({'name': 'Jai'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('It worked!')