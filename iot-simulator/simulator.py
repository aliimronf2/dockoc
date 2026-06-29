import paho.mqtt.client as mqtt
import json
import time
import random

# menentukan alamat broker MQTT
broker_address = "localhost"

# membuat identitas sensor
client = mqtt.Client("Truk_Pendingin_01")

# menghubungkan sensor ke makelas
client.connect(broker_address, 1883)

print("Memulai simulasi sensor suhu...")

while True:
    # membuat suhu acak antara -5 hingga +5
    suhu = round(random.uniform(-5.0, 5.0), 2)

    # membungkus data dalam format JSON
    payload = {
        "vehicle_id": "TRUK_L1234XYZ",
        "container_id": "CONT-001",
        "temperature_c": suhu,
        "timestamp": int(time.time() * 1000)
    }

    # mengirim JSON ke saluran "iot/sensor/suhu"
    client.publish("iot/sensor/suhu", json.dumps(payload))
    print(f"Data terkirim: {payload}")

    # istirahat 30 detik
    time.sleep(30)