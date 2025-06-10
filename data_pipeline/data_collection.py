import random
import time

def collect_behavioral_data(device_id):
    return {
        "device_id": device_id,
        "timestamp": int(time.time()),
        "fingerprint": f"fp_{random.randint(1000,9999)}",
        "biometrics": {
            "touch_pressure": random.uniform(0.1, 1.0),
            "swipe_speed": random.uniform(0.1, 3.0),
        },
        "context": {
            "location": "sample_location",
            "network_type": random.choice(["4G", "5G", "WiFi"])
        }
    }

if __name__ == "__main__":
    for i in range(5):
        print(collect_behavioral_data(f"device_{i}"))