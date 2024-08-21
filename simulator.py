import subprocess, json
from tempfile import NamedTemporaryFile

bundle_id = "kng2.cc.try-push"
device_id = "779AB5FF-B097-4D29-BC46-6BE8BC0DCCC8"  # simulator

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

