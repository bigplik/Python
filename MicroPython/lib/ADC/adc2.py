import machine, time
from machine import ADC

adc = ADC(machine.Pin(32))          # create ADC object on ADC pin
adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)

while True:
    adc.read()# read value using the newly configured attenuation and width
    print(adc.read())
    #time.sleep(8)