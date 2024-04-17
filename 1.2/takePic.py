#coding:utf-8
import cv2
import time
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
while (1):
  picTimeStamp = str(int(time.time()))
  cv2.imwrite("/home/maiga/Desktop/webtest/IOT/1.2/images/image_" + picTimeStamp + ".jpg", frame)
  print("save successfuly!")
  time.sleep(5)
