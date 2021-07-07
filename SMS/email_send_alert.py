import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	user = "bigplik@gmail.com"
	msg['from'] = user
	password = "low1274low1274"

	server = smtplib.SMTP("smtp.gmail.com", 465)
	server.startttls()
	server.login(user,password)

	server.quit()

	email_alert("hey", "hello here", "bigplik@gmail.com")
