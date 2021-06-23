import machine, ssd1306, bme280
from time import sleep

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#fill 0 (black), fill 1 (white)
oled.fill(1)
#last number belowe (0 or 1 i otional, 0 is black, 1 i white font
oled.text('Hello, World 1!', 0, 0, 0)
oled.show()


#for Pico scl=21, sda=20 and i2c line below
#i2c = machine.I2C(0, scl=machine.Pin(4), sda=machine.Pin(5))
#for ESP32 scl=4, sda=5 and i2c without argument 0
i2c2 = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
bme = bme280.BME280(i2c=i2c2)

oled.rotate(1)

while True:
    oled.fill(0)
    pressure = str(bme.pressure)
    temp = str(bme.temp)
    oled.text('from BME280', 20, 0)
    oled.text(temp + 'C', 20, 20)
    oled.text(pressure + 'hPa', 20, 40)
    oled.show()
    sleep(2)

