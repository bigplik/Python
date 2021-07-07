#wifi commands for node/slave connected to existing network by eg. home router
'''
import network, wlan = network.WLAN(network.STA_IF), wlan.active(True), wlan.scan()
wlan.ifconfig(), wlan.connect("ssid","password"), wlan.isconnected()
'''
import network, umail

kasia = 'mkacha@tlen.pl'
pawel = 'bigplik@gmail.com'
mycom = 'bigplik@my.com'
send_to = mycom
message = 'roslinka Kasi, podlej mnie 2 sdafads'

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
