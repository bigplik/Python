import sht11, machine
from machine import Pin
from sht11 import SHT11

sck = 17
data = 16
#pin sck and data used, change with yours
sht = sht11.SHT11(sck=sck, data=data)

#read temperature and humidity
tempOut = sht.temperature
humOut = sht.humidity()

#print temperature and humidity
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')