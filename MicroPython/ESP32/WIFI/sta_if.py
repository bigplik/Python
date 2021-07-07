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

def connect_to_wifi(wlan, ssid, password):
    if not wlan.isconnected():
        print("Connecting ....")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connect_to_wifi(wlan, "kilimanjarro", "kasiapaweldaciamelamerc")

if wlan.isconnected():
    print(wlan.ifconfig())