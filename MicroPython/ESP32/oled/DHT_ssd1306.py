import machine, ssd1306, dht
from time import sleep

#OLED
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#DHT
sensor = dht.DHT22(machine.Pin(0))
#sensor = dht.DHT11(Pin(14))

#DHT logic
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    #print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    print()
    oled.fill(0)
    oled.text('Temp: %3.1f C' %temp, 20, 20)
    oled.text('Humi: %3.1f %%' %hum, 20, 40)
    oled.show()
  except OSError as e:
    print('Failed to read sensor.')


#OLED display info text
#fill 0 (black), fill 1 (white)
#oled.fill(1)
#last number belowe (0 or 1 i otional, 0 is black, 1 i white font
#oled.text('Hello, World 1!', 0, 0, 0)
#oled.show()



