import umail

smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True, username='bigplik@gmail.com', password = 'low1274low1274') # Gmail's SSL port
#smtp.login('bigplik@gmail.com', 'low1274low1274')
smtp.to('bigplik@my.com')
smtp.send("dafasf")
smtp.quit()