import RPi.GPIO as GPIO

class GasSensor:
    def __init__(self, pin=16):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read(self):
        return GPIO.input(self.pin)
    
    def is_detected(self):
        return self.read() == GPIO.LOW
