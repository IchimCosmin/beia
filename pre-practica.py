# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:00:58 2024

@author: PC
"""


import random
import time
import json
import paho_mqtt.client as mqtt  # Corectarea importului
import signal
import sys

# Function to simulate temperature readings
def simulate_temperature():
    return round(random.uniform(20.0, 25.0), 2)

# Function to simulate air quality readings
def simulate_air_quality():
    return round(random.uniform(0.0, 100.0), 2)

# MQTT Configuration
mqtt_broker = "82.78.81.188"
mqtt_port = 1883
mqtt_topic = "/training/device/Ichim-Cosmin/"

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

def signal_handler(sig, frame):
    print('Disconnecting from MQTT broker...')
    client.disconnect()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

try:
    while True:
        temperature = simulate_temperature()
        air_quality = simulate_air_quality()

        sensor_data = json.dumps({
            "temperature": temperature,
            "air_quality": air_quality
        })

        client.publish(mqtt_topic, sensor_data)
        print(f"Published: {sensor_data}")

        time.sleep(60)

except KeyboardInterrupt:
    signal_handler(None, None)

print("Simulation stopped")


