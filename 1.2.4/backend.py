#coding:utf-8
import web
import Adafruit_DHT
import time
import os
import glob 
import threading
import cv2
import RPi.GPIO as GPIO


sensor = Adafruit_DHT.DHT11
pin = 26
y=13
detector_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(detector_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

temp = ""
humi = ""

cap = cv2.VideoCapture(0)

urls = (
  '/', 'index', '/pic', 'pic', '/openL', 'openL', '/closeL', 'closeL'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)


def getNewImgPath():
    file_list = glob.glob('/home/maiga/Desktop/webtest/PIC/*')
    newest_file = max(file_list, key = os.path.getctime)
    return newest_file
  
def useCamera():
    while (cap.isOpened()):
        for i in range(10):
            cap.grab()
        ret, frame = cap.read()
        picTimeStamp = str(int(time.time()))
        cv2.imwrite("/home/maiga/Desktop/webtest/PIC/" + picTimeStamp + ".jpg", frame)
        print("save successfuly!")
        time.sleep(5)

takePic = threading.Thread(target = useCamera)


class index:
    def GET(self):
        global temp, humi
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            temp = '{:.1f}°C'.format(temperature)
            humi = '{:.1f}%'.format(humidity)
        if (GPIO.input(detector_pin) == GPIO.HIGH):
            motion_string = 'Attention! Motion Detected!'
        else:
            motion_string = 'Seems that nothing moves.'
        return render.index(temp, humi, motion_string)
        
        
class pic:
    def GET(self):
        path = getNewImgPath()
        with open(path, 'rb') as f:
            img_data = f.read()
        web.header('Content-Type', 'image/jpg')
        return img_data
        
def openLight():
    GPIO.output(y,GPIO.HIGH)
    return
  
def closeLight():
    GPIO.output(y,GPIO.LOW)
    return

class openL:
    def GET(self):
        openLight()
        return

class closeL:
    def GET(self):
        closeLight()
        return

if __name__ == '__main__':
    takePic.start()
    print(takePic.is_alive())
    app.run()
