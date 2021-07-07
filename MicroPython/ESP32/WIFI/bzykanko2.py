# Complete project details at https://RandomNerdTutorials.com
import machine,time

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'kilimanjarro'
password = 'kasiapaweldaciamelamerc'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = machine.Pin(22, machine.Pin.OUT)
odpowiedz = " "

state = 0

# Complete project details at https://RandomNerdTutorials.com

def web_page():
  if state == 1:
    gpio_state="OFF"
    odpowiedz ="Kochana Kasia"
  elif state == 0:
    gpio_state="ON"
    odpowiedz ="Kasiu to zaczynajmy teraz, nie jutro, ale teraz"
  elif state == 2:
    gpio_state="BOTH"
    led.value(0)
    time.sleep(200)
    led.value(1)
    time.sleep(200)

  html = """<html>
        <head> 
            <title>Bzykanko?</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
            <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
                    .button{display: inline-block; background-color: #4286f4; border: none; 
                    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                    .button2{background-color: #e7bd3b;}
                    .button3{background-color: aqua;}
            </style>
        </head>
        <body> 
            <h1>Bzykanko?</h1> 
                <p>Odpowiedź: <strong>""" + gpio_state + """</strong></p>
                <p><a href="/?led=on"><button class="button">NIE</button></a></p>
                <p><a href="/?led=off"><button class="button button2">TAK</button></a></p>
                <p><a href="/?led=both"><button class="button button3">2w1</button></a></p>
        </body>
    </html>"""
    
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  led_both = request.find('/?led=both')
  if led_on == 6:
    print('LED OFF')
    state = 1
  if led_off == 6:
    print('LED ON')
    state = 0
  if led_both == 6:
    print('LED BOTH')
    state = 2
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

