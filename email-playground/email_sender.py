import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path

html = Template(Path("index.html").read_text())

user = input("enter your email: ")
pword = input("enter your password: ")

send_to = input("enter the email of the person you want to email: ")
subject = input("Enter a subject line: ")
user_name = input("enter your name: ")
amount = int(input("how many emails do you want to send? "))


email = EmailMessage()
email['from'] = user_name
email['to'] = send_to
email['subject'] = subject

email.set_content(html.substitute(name = user_name), 'html')

for i in range(amount):
	with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(user, pword)
		smtp.send_message(email)
		print(f"sent {i} email(s). ")

