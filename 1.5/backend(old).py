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
dht11 = DHT11()
fan = Fan()
led = LED()
gasDetec = GasSensor()
motionDetec = MotionSensor()

urls = (
  '/', 'index', '/pic', 'pic', '/openL', 'openL', '/closeL', 'closeL', 
  '/openF', 'openF', '/closeF', 'closeF'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)


class index:
    def GET(self):
        dht11.read()
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
        
        
class pic:
    def GET(self):
        path = camera.get_latest_pic()
        with open(path, 'rb') as f:
            pic_data = f.read()
        web.header('Content-Type', 'image/jpg')
        return pic_data
        
class openL:
    def GET(self):
        led.open_all()
        return

class closeL:
    def GET(self):
        led.close_all()
        return

class openF:
    def GET(self):
        fan.open()
        return
    
class closeF:
    def GET(self):
        fan.close()
        return

if __name__ == '__main__':
    thread_start_capture = threading.Thread(target = camera.start_capture)
    thread_start_capture.start()
    app.run()
