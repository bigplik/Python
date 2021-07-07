import esp32,time

tf = esp32.raw_temperature()
tc = (tf-32.0)/1.8

while True:
    print("T = {0:4d} deg F or {1:5.1f}  deg C".format(tf,tc))
    print("{:.1f}".format(tc))
    time.sleep(2)