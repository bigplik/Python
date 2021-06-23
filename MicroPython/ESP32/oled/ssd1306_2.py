import machine
import utime

#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)
#oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#fill 0 (black), fill 1 (white)
#For Pico scl=21, sda=20
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
#print(i2c.scan())
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(0)
#last number belowe (0 or 1 i otional, 0 is black, 1 i white font
oled.text('Hello, World 1!', 0, 0, 1)
oled.show()