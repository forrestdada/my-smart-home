#coding:utf-8
import web
import Adafruit_DHT
import time
import os
import glob 
import threading
import cv2

sensor = Adafruit_DHT.DHT11
pin = 26

temp = ""
humi = ""

cap = cv2.VideoCapture(0)

urls = (
  '/', 'index', '/pic', 'pic'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)


def getNewImgPath():
    file_list = glob.glob('/home/maiga/Desktop/webtest/IOT/1.2.1/images/*')
    newest_file = max(file_list, key = os.path.getctime)
    return newest_file
  
def useCamera():
    while (cap.isOpened()):
        for i in range(10):
            cap.grab()
        ret, frame = cap.read()
        picTimeStamp = str(int(time.time()))
        cv2.imwrite("/home/maiga/Desktop/webtest/IOT/1.2.1/images/" + picTimeStamp + ".jpg", frame)
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
        return render.index(temp, humi)
        
        
class pic:
    def GET(self):
        path = getNewImgPath()
        with open(path, 'rb') as f:
            img_data = f.read()
        web.header('Content-Type', 'image/jpg')
        return img_data

if __name__ == '__main__':
    takePic.start()
    print(takePic.is_alive())
    app.run()
