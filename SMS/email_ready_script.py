import smtplib
print("\nthis email sender is working only with google accounts \n")

sender = "bigplik@gmail.com"
reciever = input("to who want to send it? \n")
subject = input("what is the subject? \n")
message_text = input("put your message here \n")
message = "Subject: {:} \r\nTo: %s\r\n\r\n".format(subject) + message_text
login = input("what is your login? \n")
password = input("jakie haslo? \n")

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(login,password)
server.sendmail(sender,reciever,message)
server.quit()

print("message from " + sender + " was sent to {:}".format(reciever))

