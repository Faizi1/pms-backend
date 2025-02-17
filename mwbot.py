import paho.mqtt.client as mqtt
import json
import time
import random
from django.conf import settings

# Dummy MWbot Configuration
BOT_ID = 1
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Dummy MWbot connected to MQTT Broker (rc={rc})")
    client.subscribe(f"mwbot/dispatch/{BOT_ID}")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    spot_id = payload.get("spotID")
    action = payload.get("action")

    statuses = ["moving", "charging", "completed"]
    if action == "dispatch":
        print(f"MWbot received dispatch command for Spot {spot_id}")
        simulate_charging_process(client, spot_id)

    for status in statuses:
        time.sleep(random.randint(2, 5))  # Simulate MWbot movement and charging process
        message = json.dumps({"botID": BOT_ID, "status": status, "spotID": spot_id})
        client.publish(f"mwbot/status/{BOT_ID}", message)
        print(f"MWbot updated status: {status}")

    

# MQTT Client for Dummy MWbot
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

print("Dummy MWbot is running and listening for dispatch commands...")
