import time

import requests
import json

url = "https://chirpstack-api.iotserv.ru/api/devices"

for count in range(1, 3):
    hex_str = format(count, 'X')
    description = f"Test Device from KAA{count}"
    devEui = f"0{hex_str}192233445566FF"
    my_dump = {
        "device": {
            "applicationId": "22581d62-7777-429a-b816-12bf56f35f6e",
            "description": description,
            "devEui": devEui,
            "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
            "isDisabled": False,
            "joinEui": "0000000000000000",
            "name": description,
            "skipFcntCheck": False
        }
    }

    payload = json.dumps(my_dump)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjA5MDRmZjExLWFhZDAtNDJlYy05YmEyLTQ3ZDIzMmZmZDgyOSIsInR5cCI6ImtleSJ9.5kQMDUtyio2Ve-yIH2al3BbaEAhQa9XDdR8Klmzifx0'
    }

    success = False
    trial_count = 0
    while not success:
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            response.raise_for_status()
            success = True
        except requests.exceptions.RequestException as e:
            response_dict = response.json()
            if response_dict.get('code') == 13:  # Conflict status code for duplicate entry
                print(f"Error: Duplicate entry for devEui {devEui}. Skipping.")
                success = True  # Proceed to the next iteration
            elif response.status_code == 200 or response.status_code == 201:
                success = True
            else:
                if trial_count > 3:
                    print("Max retries reached. Skipping this request.")
                    break
                trial_count += 1
                print("Retrying in 5 seconds...")
                time.sleep(5)  # Wait for 5 seconds before retrying
    print(response.status_code)
