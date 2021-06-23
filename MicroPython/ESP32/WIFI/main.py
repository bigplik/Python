#to work save it on board as main.py
import network, ntptime, time
from machine import RTC

DATETIME_ELEMENTS = {
    "year": 2021,
    "month": 1,
    "day": 2,
    "day_of_week": 3,
    "hour": 4,
    "minute": 5,
    "second": 6,
    "millisecond": 7,
}
'''
new = {
    "one" : 1,
    2: "two"
    }
'''
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

now = time.time()
tm = time.localtime(now)
print("localtime " + str(tm))

year, month, day, hour, minute, second, ms, dayinyear = time.localtime()

'''
set_datetime_element(rtc, "month", 6)
set_datetime_element(rtc, "day", 13)
set_datetime_element(rtc, "hour", 13)
'''
#print(DATETIME_ELEMENTS["month"])
print(year, month, day)

while True:
    year, month, day, hour, minute, second, ms, dayinyear = time.localtime()
    hour = hour + 2 #2 hours plus as zone adjust
    print(hour, minute, second)
    time.sleep(1)

