#!/usr/bin/env python3
import os
import requests

APP_NAME = os.environ.get("APP_NAME")
APP_URL = os.environ.get("APP_URL", f"http://localhost:7878")
KEY_OUTPUT_PATH = os.environ.get("KEY_OUTPUT_PATH", f"/opt/central-api-keys/{APP_NAME}.key")

def get_api_key():
    try:
        response = requests.get(f"{APP_URL}/api/v3/system/status")
        if response.status_code == 200:
            data = response.json()
            api_key = data.get("apiKey", "NOT_FOUND")
            if api_key != "NOT_FOUND":
                os.makedirs(os.path.dirname(KEY_OUTPUT_PATH), exist_ok=True)
                with open(KEY_OUTPUT_PATH, "w") as f:
                    f.write(api_key)
                print(f"[{APP_NAME}] API key saved to {KEY_OUTPUT_PATH}")
            else:
                print(f"[{APP_NAME}] API key not found in response.")
        else:
            print(f"[{APP_NAME}] Failed to fetch API key: {response.status_code}")
    except Exception as e:
        print(f"[{APP_NAME}] Error retrieving API key: {e}")

if __name__ == "__main__":
    get_api_key()
