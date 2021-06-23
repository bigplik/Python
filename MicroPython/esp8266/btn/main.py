import machine
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

button.value()