import cv2
import time
import os
import glob

class Camera:
    def __init__(self, pic_path="/home/maiga/Desktop/webtest/PIC/", interval=1):
        self.cap = cv2.VideoCapture(0)
        self.pic_path = pic_path
        self.interval = interval
        self.latest_pic = None

        # 确保输出文件夹存在
        if not os.path.exists(self.pic_path):
            os.makedirs(self.pic_path)

    def capture_pic(self):
        ret, frame = self.cap.read()
        if not ret:
            return False

        # 保存图片到指定文件夹
        timestamp = str(int(time.time()))
        output_path = self.pic_path + timestamp + ".jpg"
        cv2.imwrite(output_path, frame)
        return True

    def get_latest_pic(self):
        file_list = glob.glob('/home/maiga/Desktop/webtest/PIC/*')
        self.latest_pic = max(file_list, key = os.path.getctime)
        return self.latest_pic     

    def start_capture(self):
        while True:
            self.capture_pic()
            time.sleep(self.interval)
            #print('capture successfully!')

    def release(self):
        self.cap.release()

if __name__ == "__main__":
    camera = Camera()
    try:
        camera.start_capture()
    except KeyboardInterrupt:
        camera.release()
