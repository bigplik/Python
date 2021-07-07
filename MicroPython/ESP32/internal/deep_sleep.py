# Complete project details at https://RandomNerdTutorials.com

import machine
from machine import Pin
from time import sleep

led = Pin (22, Pin.OUT)

#blink LED
print('Im awake')
for i in range(10):
    led.value(1)
    sleep(0.2)
    led.value(0)
    sleep(0.2)

# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
sleep(5)

print('Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
machine.deepsleep(5000)