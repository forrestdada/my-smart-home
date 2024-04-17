import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.r = 19
        self.y = 13
        self.g = 6
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.ledR = GPIO.setup(self.r, GPIO.OUT)
        self.ledY = GPIO.setup(self.y, GPIO.OUT)
        self.ledG = GPIO.setup(self.g, GPIO.OUT)


    def open(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def close(self, pin):
        GPIO.output(pin, GPIO.LOW)
        
    def open_all(self):
        GPIO.output(self.r, GPIO.HIGH)
        GPIO.output(self.y, GPIO.HIGH)
        GPIO.output(self.g, GPIO.HIGH)
        
    def close_all(self):
        GPIO.output(self.r, GPIO.LOW)
        GPIO.output(self.y, GPIO.LOW)
        GPIO.output(self.g, GPIO.LOW)
    
