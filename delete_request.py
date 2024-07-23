import requests

for count in range(1, 3):
    hex_str = format(count, 'X')
    url = f"https://chirpstack-api.iotserv.ru/api/devices/0{hex_str}192233445566ff"

    payload = {}
    headers = {
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjA5MDRmZjExLWFhZDAtNDJlYy05YmEyLTQ3ZDIzMmZmZDgyOSIsInR5cCI6ImtleSJ9.5kQMDUtyio2Ve-yIH2al3BbaEAhQa9XDdR8Klmzifx0'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.status_code)
