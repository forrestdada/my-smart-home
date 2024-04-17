import web
import Adafruit_DHT
import time
sensor = Adafruit_DHT.DHT11
pin = 26

temp = "30°C"
humi = "30%"

urls = (
  '/', 'index'
)

render = web.template.render('web/')
app = web.application(urls, globals(), True)

    
class index:
    def GET(self):
        global temp, humi
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            temp = '{:.1f}°C'.format(temperature)
            humi = '{:.1f}%'.format(humidity)
        return render.index(temp, humi)

if __name__ == '__main__':
    app.run()
