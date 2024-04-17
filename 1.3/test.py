#camera test
'''
from hardware.camera import Camera

camera = Camera()

print(camera.pic_path)
print(camera.interval)
print(camera.latest_pic)

camera.capture_pic()
print(camera.latest_pic)
print(camera.get_latest_pic())

#camera.start_capture()
'''


#dhttest
'''
from hardware.dht_11 import DHT11

dht11 = DHT11()

dht11.read()

print(dht11.temperature)
print(dht11.humidity)
print(dht11.get_temperature())
print(dht11.get_humidity())
'''

#fan test
'''
import time
from hardware.fan import Fan
fan = Fan()
print(1)
time.sleep(5)
fan.open()
time.sleep(5)
fan.close()
'''

#led test
'''c
import time
from hardware.led import LED
led = LED()
print(1)
led.open(led.r)
time.sleep(1)
led.open(led.y)
time.sleep(1)
led.open(led.g)
time.sleep(1)
led.close(led.r)
time.sleep(1)
led.close(led.y)
time.sleep(1)
led.close(led.g)
time.sleep(1)
led.open_all()
time.sleep(1)
led.close_all()
'''


#gas detec test
'''
from hardware.gas_detector import GasSensor
import time
gasDetec = GasSensor()
while True:
    print(gasDetec.read())
    print(gasDetec.is_detected())
    time.sleep(0.5)
'''


#motion detec test
'''
from hardware.motion_detector import MotionSensor
import time
motionDetec = MotionSensor()
while True:
    print(motionDetec.read())
    print(motionDetec.is_detected())
    time.sleep(0.5)
'''



