import requests

url = "https://chirpstack-api.iotserv.ru/api/devices?limit=10&applicationId=22581d62-7777-429a-b816-12bf56f35f6e"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjA5MDRmZjExLWFhZDAtNDJlYy05YmEyLTQ3ZDIzMmZmZDgyOSIsInR5cCI6ImtleSJ9.5kQMDUtyio2Ve-yIH2al3BbaEAhQa9XDdR8Klmzifx0'
}

try:
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    response_list = response.json().get('result', [])
    if not response_list:
        print("No devices found.")
    else:
        count = 1
        for get_request in range(10):
            my_dict1 = dict(response_list[0])
            my_dict2 = dict(response_list[1])

            result = f"{count:02}. Status: {response.status_code} Device name: {my_dict1.get('name')}, description: {my_dict2.get('name')}"
            count += 1
            print(result)
except requests.exceptions.RequestException as e:
    print(f'Request failed: {e}')
