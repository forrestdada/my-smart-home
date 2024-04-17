import Adafruit_DHT

class DHT11:
    def __init__(self, pin = 26):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        self.temperature = None
        self.humidity = None

    def read(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity
