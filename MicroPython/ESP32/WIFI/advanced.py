#to work save it on board as main.py
import network, ntptime
from machine import RTC

DATETIME_ELEMENTS = {
    "year": 0,
    "month": 1,
    "day": 2,
    "day_of_week": 3,
    "hour": 4,
    "minute": 5,
    "second": 6,
    "millisecond": 7,
}

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

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connect_to_wifi(wlan, "kilimanjarro", "kasiapaweldaciamelamerc")

rtc = RTC()
ntptime.settime()
print(rtc.datetime())

set_datetime_element(rtc, "month", 6)
set_datetime_element(rtc, "day", 13)
set_datetime_element(rtc, "hour", 13)
print(rtc.datetime())