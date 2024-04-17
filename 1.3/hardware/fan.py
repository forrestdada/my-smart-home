import RPi.GPIO as GPIO

class Fan:
    def __init__(self, pin=17):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)

    def open(self):
        GPIO.output(self.pin, GPIO.LOW)

    def close(self):
        GPIO.output(self.pin, GPIO.HIGH)
