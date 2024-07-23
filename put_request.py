import requests
import json

for count in range(1, 3):
    hex_str = format(count, 'X')
    url = f"https://chirpstack-api.iotserv.ru/api/devices/0{hex_str}192233445566FF"

    payload = json.dumps({
      "device": {
        "applicationId": "22581d62-7777-429a-b816-12bf56f35f6e",
        "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
        "name": f"Test Device from KAA{count} UPDATED"
      }
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjA5MDRmZjExLWFhZDAtNDJlYy05YmEyLTQ3ZDIzMmZmZDgyOSIsInR5cCI6ImtleSJ9.5kQMDUtyio2Ve-yIH2al3BbaEAhQa9XDdR8Klmzifx0'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.status_code)
