# Complete project details at https://RandomNerdTutorials.com

import machine, network, umail
from time import sleep

kasia = 'mkacha@tlen.pl'
pawel = 'bigplik@gmail.com'
mycom = 'bigplik@my.com'
send_to = mycom
message = 'deep sleep test text'

def connect_to_wifi(wlan, ssid, password):
    if not wlan.isconnected():
        print("Connecting ....")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

def send_message():
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True, username='bigplik@gmail.com', password = 'low1274low1274') # Gmail's SSL port
    smtp.to(send_to, "pJdafdsf")
    #smtp.write('test') #can be used instead of smtp.send()
    smtp.write("Subject: Poem\n") #subject
    smtp.send(message)
    smtp.quit()
    print(message)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connect_to_wifi(wlan, "kilimanjarro", "kasiapaweldaciamelamerc")
if wlan.isconnected():
    print(wlan.ifconfig())
send_message()


# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
#sleep(5)

print('Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
machine.deepsleep(5000)
