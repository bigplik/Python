#send email
import smtplib

message = "to jest wiadomosc esp32 from python3 sublime text"

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("bigplik@gmail.com","low1274low1274")
server.sendmail("bigplik@gmail.com","bigplik@gmail.com", message)
server.quit()
