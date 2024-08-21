"""Utility functions for sending push notifications to APNs"""

import jwt
import time
from httpx import Response, Client
from typing import Literal

EndPt = Literal["Sandbox", "Production"]


def create_jwt_token(auth_key: str, team_id: str, key_id: str) -> str:
    """Create JWT token for APNs"""
    token = jwt.encode(
        {
            "iss": team_id,
            "iat": time.time(),
        },
        auth_key,
        algorithm="ES256",
        headers={
            "alg": "ES256",
            "kid": key_id,
        },
    )
    return token


def create_payload(title: str, subtitle: str, body: str, userInfo: str) -> dict:
    """Create APNs payload"""
    return {
        "aps": {
            "alert": {
                "title": title,
                "subtitle": subtitle,
                "body": body,
            },
            "sound": "default",
        },
        "userInfo": userInfo,
    }


def send_push_notification(
    apns_topic: str, device_token: str, endpoint: EndPt, payload: dict, jwt_token: str
) -> Response:
    """Send a push notification"""

    headers = {
        "apns-topic": apns_topic,
        "authorization": f"bearer {jwt_token}",
    }

    domain = "" if endpoint == "Production" else ".sandbox"

    url = f"https://api{domain}.push.apple.com/3/device/{device_token}"

    # Use httpx.Client with HTTP/2 support
    with Client(http2=True) as client:
        response = client.post(url, headers=headers, json=payload)

    return response
