import paho.mqtt.client as mqtt
from config import config



def set_time_of_use(point, category, value):
    client = mqtt.Client("solar-controller")
    client.connect(config["solar_assistant"]["ip"])
    client.publish(f"solar_assistant/inverter_1/{category}_point_{point}/set", value)
