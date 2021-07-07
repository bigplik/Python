import smtplib

send_to = input("to whom want to send? ")
message = input("what to send? \n")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("bigplik@gmail.com", "low1274low1274")
server.sendmail(
  "bigplik@gmail.com", #"from@address.com", 
  send_to, #"to@address.com", 
  message) #"this message is from python"#message)
server.quit()