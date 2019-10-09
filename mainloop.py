
import json
import utils.mqttconnection as mqttconn
from timeloop import Timeloop
from datetime import timedelta
from datetime import datetime

tl = Timeloop()
mqttc = None

@tl.job(interval=timedelta(seconds=1))
def sample_job():
    mqttc.publish("topic/test", "ts: %d\r\n" %( datetime.timestamp(datetime.now()) ), qos=0, retain=False)


if __name__ == "__main__":

    with open('./config/config.json') as json_data_config:
        config_data = json.load(json_data_config)
    
    host=config_data["host"]
    port=config_data["port"]
    username=config_data["username"]
    password=config_data["password"]

    #open mqtt connection using username and password
    mqtt = mqttconn.MqttConnection(host, port, username, password)
    mqttc = mqtt.getClient()



