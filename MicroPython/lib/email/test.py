#wifi commands for node/slave connected to existing network by eg. home router
'''
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.ifconfig()
wlan.connect("ssid","password")
wlan.isconnected()
'''
import network, umail

send_to = 'bigplik@my.com'

def connect_to_wifi(wlan, ssid, password):
    if not wlan.isconnected():
        print("Connecting ....")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

def send_message():
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True, username='bigplik@gmail.com', password = 'low1274low1274') # Gmail's SSL port
    smtp.to(send_to)
    smtp.send("sent from Thonny_IDE")
    smtp.quit()
    print("your message to " + send_to + " has just been sent")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connect_to_wifi(wlan, "kilimanjarro", "kasiapaweldaciamelamerc")

if wlan.isconnected():
    print(wlan.ifconfig())
    
send_message()