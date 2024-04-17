import paho.mqtt.client as mqtt

class DHT11:
    def __init__(self, mqtt_server, mqtt_port=1883, temp_topic="esp/dht/temperature", hum_topic="esp/dht/humidity"):
        self.mqtt_server = mqtt_server
        self.mqtt_port = mqtt_port
        self.temp_topic = temp_topic
        self.hum_topic = hum_topic

        self.temperature = None
        self.humidity = None

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.mqtt_server, self.mqtt_port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT server with result code {rc}")
        self.client.subscribe(self.temp_topic)
        self.client.subscribe(self.hum_topic)

    def on_message(self, client, userdata, msg):
        if msg.topic == self.temp_topic:
            self.temperature = float(msg.payload.decode("utf-8"))
        elif msg.topic == self.hum_topic:
            self.humidity = float(msg.payload.decode("utf-8"))

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
