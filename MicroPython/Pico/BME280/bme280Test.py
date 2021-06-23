import machine
from time import sleep
import bme280

i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))
bme = bme280.BME280(i2c=i2c)

while True:
    print(bme.values)
    sleep(20)