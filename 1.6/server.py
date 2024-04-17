#coding:utf-8
import web
import threading
import time

from hardware.camera import Camera
from hardware.dht_11 import DHT11
from hardware.fan import Fan
from hardware.led import LED
from hardware.gas_detector import GasSensor
from hardware.motion_detector import MotionSensor

camera = Camera()
dht11 = DHT11('192.168.3.6')
fan = Fan('192.168.3.6')
led = LED()
gasDetec = GasSensor()
motionDetec = MotionSensor()

urls = (
  '/', 'Index', 
  '/temperature', 'Temperature', 
  '/humidity', 'Humidity', 
  '/gas', 'Gas',
  '/pic', 'Pic', 
  '/openL', 'OpenL', 
  '/closeL', 'CloseL', 
  '/openF', 'OpenF', 
  '/closeF', 'CloseF'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)


class Index:
    def GET(self):
        motionDetec.read()
        gasDetec.read()
        
        temp = str(dht11.temperature) + '°C' 
        humi = str(dht11.humidity) + '%'
        
        if motionDetec.is_detected():
            motion_string = 'Attention! Motion Detected!'
        else:
            motion_string = 'Seems that nothing moves.'
        
        if gasDetec.is_detected():
            gas_string = 'Gas Detected!'
        else:
            gas_string = 'No Gas Leak.'
        
        return render.index(temp, humi, motion_string, gas_string)
        

class Temperature:
    def GET(self):
        return dht11.temperature
    
class Humidity:
    def GET(self):
        return dht11.humidity
    
class Gas:
    def GET(self):
        gasDetec.read()
        return gasDetec.is_detected

class Pic:
    def GET(self):
        path = camera.get_latest_pic()
        with open(path, 'rb') as f:
            pic_data = f.read()
        web.header('Content-Type', 'image/jpg')
        return pic_data
        
class OpenL:
    def GET(self):
        led.open(led.r)
        return

class CloseL:
    def GET(self):
        led.close(led.r)
        return

class OpenF:
    def GET(self):
        fan.open()
        return
    
class CloseF:
    def GET(self):
        fan.close()
        return
        
def autoLightInBathroom():
    while True:
        if motionDetec.is_detected():
            led.open(led.y)
            time.sleep(5)
            led.close(led.y)
        else:
            led.close(led.y)


if __name__ == '__main__':
    thread_capture = threading.Thread(target = camera.start_capture)
    thread_autoLight = threading.Thread(target = autoLightInBathroom)
    thread_capture.start()
    thread_autoLight.start()
    
    try:
        app.run()
    
    except KeyboardInterrupt:
        led.close(led.r)
        led.close(led.y)
        GPIO.cleanup()
        fan.disconnect()
        dht11.disconnect()

