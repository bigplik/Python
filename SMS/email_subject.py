import smtplib

message_text = "some body text here"
sender = "bigplik@gmail.com"
reciever = "bigplik@my.com"
message = "Subject: Poem \r\nTo: %s\r\n\r\n" + message_text

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("bigplik@gmail.com","low1274low1274")
server.sendmail(sender,reciever,message)
server.quit()

