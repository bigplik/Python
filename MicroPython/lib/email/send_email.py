#send email
import smtplib

password = input("what is your password? then press enter: ")

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("bigplik@gmail.com",password)
server.sendmail("bigplik@my.com","bigplik@my.com", "hi here is an email from esp32_micropython")
server.quit()
