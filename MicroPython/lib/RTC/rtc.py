from machine import RTC
import time

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # set a specific date and time
rtc.datetime() # get date and time
print(rtc.datetime())

year, month, day, hour, minute, second, ms, dayinyear = time.localtime()

while True:
    #print(time.localtime())
    year, month, day, hour, minute, second, ms, dayinyear = time.localtime()
    print(hour, minute, second)
    time.sleep(1)