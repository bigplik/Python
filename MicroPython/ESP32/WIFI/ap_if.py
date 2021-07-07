#wifi commands for master access point mode
import network
password = "1234"

wlan = network.WLAN(network.AP_IF)
wlan.config(essid="Agathocles_KURWA_MAC!!", password = password)
wlan.active(True)

print('Connection successful')
print(wlan.ifconfig())