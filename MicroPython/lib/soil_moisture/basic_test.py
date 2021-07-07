#soil moisture sensor adc
from machine import Pin, ADC
from time import sleep


soil_moisture = ADC(Pin(32))
soil_moisture.atten(ADC.ATTN_11DB)    # set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
soil_moisture.width(ADC.WIDTH_12BIT)   # set 12 bit return values (returned range 0-4095)     
    
def remap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def soil_reader():
    soil_moisture_value = remap(
        soil_moisture.read(),
        700, 3350,     # these values comes from experiment above when wet and dry
        100, 1          # or you can map to whatever values you wish
    )
    print("Soil plant Humidity {:.2f}%".format(soil_moisture_value))
    
while True:
    soil_reader()
    print("raw value " + str(soil_moisture.read()))
    #print(str(soil_moisture_value) + "%")
    sleep(2)