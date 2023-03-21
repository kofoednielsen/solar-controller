import paho.mqtt.client as mqtt
from config import config


def set_time_of_use_voltage_point(point, voltage):
    client = mqtt.Client("solar-controller")
    client.connect(config["solar_assistant"]["ip"])
    client.publish(f"solar_assistant/inverter_1/voltage_point_{point}/set", voltage)
