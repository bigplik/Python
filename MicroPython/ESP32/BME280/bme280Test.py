import machine, bme280
from time import sleep


#for Pico scl=21, sda=20 and i2c line below
#i2c = machine.I2C(0, scl=machine.Pin(4), sda=machine.Pin(5))
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
bme = bme280.BME280(i2c=i2c)

while True:
    print(bme.values)
    print("temp", bme.temp)
    print("hpa ", bme.pressure)
    print()
    sleep(2)