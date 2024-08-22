"""using `xcrun simctl push` command to send push notification to simulator or device"""

import subprocess, json
from tempfile import NamedTemporaryFile

bundle_id = "your.bundle.id"

# find in Xcode -> Window -> Device and Simulator
device_id = "simulator-or-device-uuid"  

payload = {
    "Simulator Target Bundle": bundle_id,
    "aps": {
        "alert": {
            "title": "Push Reward 💨",
            "subtitle": "go to home page",
        },
        "sound": "default",
    },
    "url": "/RewardHome",
}

with NamedTemporaryFile(mode='w') as apns:
    json.dump(payload, apns)
    apns.seek(0)

    cmd = ["xcrun", "simctl", "push"] + [
        device_id,
        bundle_id,
        apns.name,
    ]
    result = subprocess.run(cmd)
    print(f"{result.returncode=}")

