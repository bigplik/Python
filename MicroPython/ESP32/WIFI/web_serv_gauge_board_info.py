try:
  import usocket as socket
except:
  import socket

import network, time, esp32
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'kilimanjarro'
password = 'kasiapaweldaciamelamerc'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

tf = esp32.raw_temperature()
tc = (tf-32.0)/1.8
hum = 80

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#number and type of board data written in data.txt
f = open('data.txt')
info = f.read()

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

# Complete project details at https://RandomNerdTutorials.com

def read_sensor():
    tf = esp32.raw_temperature()
    tc = (tf-32.0)/1.8

def web_page():
  html = """<!DOCTYPE HTML><html>
<head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
        google.charts.load('current', {'packages':['gauge']});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {

            var data = google.visualization.arrayToDataTable([
                ['Label', 'Value'],
                ['Cpu Temp', 0]//,
                //['Max', 23]
            ]);

            var options = {
                width: 400, height: 400,
                minorTicks: 10,
                redFrom: 60, redTo: 80,
                yellowFrom:40, yellowTo: 60,
                min: 0,
                max: 80
            };

            var chart = new google.visualization.Gauge(document.getElementById('temp_chart'));

            setInterval(function() {
                data.setValue(0, 1, """+str("{:.1f}".format(tc))+""");
                chart.draw(data, options);
            }, 2600);
            
            /*
            setInterval(function() {
                data.setValue(1, 1, 30 + Math.round(30 * Math.random()));
                chart.draw(data, options);
            }, 2600);
            */

            chart.draw(data, options);
      }
    </script>
</head>
<body>
    <center>
    <h1>ESP32 internal temperature</h1>
    <div id="temp_chart" style="width: 400px; height: 400px;"></div>
    <h2>"""+str("{:}".format(info))+"""</h2>
    </center>
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
  print('Content = %s' % str(request))
  sensor_readings = read_sensor()
  print(sensor_readings)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
