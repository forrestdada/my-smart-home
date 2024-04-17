import RPi.GPIO as GPIO

class MotionSensor:
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def read(self):
        return GPIO.input(self.pin)

    def is_detected(self):
        return self.read() == GPIO.HIGH
