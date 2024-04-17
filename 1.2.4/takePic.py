#coding:utf-8
import cv2
import time
#import os
#import glob 

cap = cv2.VideoCapture(0)

'''
def getNewImgPath():
  file_list = glob.glob('/home/maiga/Desktop/webtest/IOT/1.2.1/images')
  newest_file = max(file_list, key = os.path.getctime)
  return os.path.basename(newest_file)
'''

while (cap.isOpened()):
  for i in range(10):
    cap.grab()
  ret, frame = cap.read()
  picTimeStamp = str(int(time.time()))
  cv2.imwrite("/home/maiga/Desktop/webtest/IOT/1.2.1/images/" + picTimeStamp + ".jpg", frame)
  print("save successfuly!")
  time.sleep(5)
