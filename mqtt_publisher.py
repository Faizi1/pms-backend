import json
import threading
import paho.mqtt.client as mqtt
from django.conf import settings

class MQTTHandler:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)

    def on_connect(self, client, userdata, flags, rc):
        """Subscribe to MWBot topics when connected."""
        print(f"✅ Connected to MQTT Broker (rc={rc})")
        client.subscribe("mwbot/status/#")
        client.subscribe("mwbot/dispatch/#")

    def on_message(self, client, userdata, msg):
        """Handles incoming MQTT messages."""
        from api.models import ChargingRequest  # Import inside function

        payload = json.loads(msg.payload.decode())
        topic = msg.topic

        if "status" in topic:
            self.update_mwbot_status(payload)
        elif "dispatch" in topic:
            self.handle_mwbot_dispatch(payload)

    def update_mwbot_status(self, payload):
        """Updates MWBot status."""
        from api.models import ChargingRequest  # Import inside function

        bot_id = payload.get("botID")
        status = payload.get("status")
        spot_id = payload.get("spotID")

        try:
            charging_request = ChargingRequest.objects.filter(bot_id=bot_id, spot_id=spot_id).first()
            if charging_request:
                charging_request.status = status
                charging_request.save()
                print(f"✅ Updated Charging Request {charging_request.id} → Status: {status}")
            else:
                print(f"⚠ No Charging Request found for MWbot ID {bot_id}")
        except Exception as e:
            print(f"❌ Error updating status: {e}")

    def start(self):
        """Start MQTT listener in a separate thread."""
        thread = threading.Thread(target=self.client.loop_forever, daemon=True)
        thread.start()
