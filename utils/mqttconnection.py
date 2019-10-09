import paho.mqtt.client as mqtt

class MqttConnection():
    
    def __init__(self, host, port, username, password):
        self.mqttc = mqtt.Client(
            client_id="",
            protocol=mqtt.MQTTv311,
            transport="tcp"
        )
        self.mqttc.username_pw_set(username, password)
        self.mqttc.connect(host, port=port)
        self.mqttc.loop_start()

    def getClient(self):
        return self.mqttc
