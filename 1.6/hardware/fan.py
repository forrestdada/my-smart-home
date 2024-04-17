import paho.mqtt.client as mqtt

class Fan:
    def __init__(self, mqtt_server, mqtt_port=1883, fan_topic="esp8266/fan"):
        self.mqtt_server = mqtt_server
        self.mqtt_port = mqtt_port
        self.fan_topic = fan_topic

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.connect(self.mqtt_server, self.mqtt_port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT server with result code {rc}")

    def open(self):
        self.client.publish(self.fan_topic, "ON")

    def close(self):
        self.client.publish(self.fan_topic, "OFF")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
