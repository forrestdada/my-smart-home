import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.r = 19
        self.y = 13
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.ledR = GPIO.setup(self.r, GPIO.OUT)
        self.ledY = GPIO.setup(self.y, GPIO.OUT)


    def open(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def close(self, pin):
        GPIO.output(pin, GPIO.LOW)
