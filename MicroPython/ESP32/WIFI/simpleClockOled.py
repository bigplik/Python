import machine, ssd1306, time, network, ntptime
from machine import RTC
from machine import Pin
from time import sleep

i2c = machine.I2C(0, scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.rotate(1)

def connect_to_wifi(wlan, ssid, password):
    if not wlan.isconnected():
        print("Connecting ....")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

def set_datetime_element(rtc, datetime_element, value):
    date = list(rtc.datetime())
    date[DATETIME_ELEMENTS[datetime_element]] = value
    rtc.datetime(date)
    #print("value" + str(value))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connect_to_wifi(wlan, "kilimanjarro", "kasiapaweldaciamelamerc")

rtc = RTC()
ntptime.settime()
print(rtc.datetime())

year, month, day, hour, minute, second, ms, dayinyear = time.localtime()

while True:
    #print(time.localtime())
    year, month, day, hour, minute, second, ms, dayinyear = time.localtime()
    hour = hour + 2  #add 3 hours as zone adjust
    #print(hour, minute, second)
    oled.fill(0)
    oled.text('Simple Clock', 20, 0)
    oled.text(str(hour)+ ":" +str(minute) + ":" +str(second), 40, 10)
    oled.show() 
    sleep(1)