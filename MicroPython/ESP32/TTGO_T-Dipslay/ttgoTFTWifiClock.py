'''
tft ttgo t-display wifi synchornized clock
'''

import machine, random, time, esp32, network, ntptime
import st7789py as st7789
from machine import Pin, SoftSPI
from machine import RTC
from time import sleep
import vga2_bold_16x32 as font



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

def main():
    spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(18),
        mosi=Pin(19),
        miso=Pin(13))

    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=0)
    
    year, month, day, hour, minute, second, ms, dayinyear = time.localtime()
    hour = hour + 2  #add 3 hours as zone adjust
    
    tft.fill(st7789.WHITE)
    tft.rotation(3)

    tft.text(font, 'Simple Clock', 20, 10, st7789.BLACK, st7789.WHITE)
    tft.text(font, str(year)+ "-" +str(month) + "-" +str(day), 48, 50, st7789.WHITE, st7789.BLACK)
        
    while True:
        year, month, day, hour, minute, second, ms, dayinyear = time.localtime()
        hour = hour + 2  #add 3 hours as zone adjust
        if second<10 and minute >10:
            tft.text(font, str(hour)+ ":" + str(minute) + ":0" + str(second), 60, 80, st7789.WHITE, st7789.BLACK)
        elif second<10 and minute<10:
            tft.text(font, str(hour)+ ":0" + str(minute) + ":0" + str(second), 60, 80, st7789.WHITE, st7789.BLACK)
        elif minute<10:
            tft.text(font, str(hour)+ ":0" + str(minute) + ":" + str(second), 60, 80, st7789.WHITE, st7789.BLACK)
        elif hour<10:
            tft.text(font, "0" + str(hour)+ ":" +str(minute) + ":" + str(second), 60, 80, st7789.WHITE, st7789.BLACK)
        else:
            tft.text(font, str(hour)+ ":" +str(minute) + ":" + str(second), 60, 80, st7789.WHITE, st7789.BLACK)
        #                                 font color    background color
        #tft.text(font, "text mode", 20, 20, st7789.WHITE, st7789.BLACK)
        #tft.text(font, 'Simple Clock', 20, 10, st7789.BLACK, st7789.WHITE)
        #tft.text(font, str(year)+ "-" +str(month) + "-" +str(day), 48, 50, st7789.WHITE, st7789.BLACK)
#         tft.text(font, str(hour)+ ":" +str(minute) + ":" +printsecond, 65, 80, st7789.WHITE, st7789.BLACK)
        #print("done")
        time.sleep(1)

main()

def clock():
    tft.text(font,"zegar", 60, 60, st7789.WHITE, st7789.BLACK)
