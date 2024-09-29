import requests

url = 'http://localhost:8000/payments/search'
local = 0
if local:
    url = 'http://localhost:8000/payments/search'
else:
    url = 'http://54.83.149.21:8003/payments/search'
data = {"user_id": "123456"}
response = requests.post(url, json=data)
print(response.text)