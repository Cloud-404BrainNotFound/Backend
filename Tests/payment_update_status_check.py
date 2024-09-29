import requests

url = 'http://localhost:8000/payments/update_status'
local = 0
if local:
    url = 'http://localhost:8000/payments/update_status'
else:
    url = 'http://54.83.149.21:8003/payments/update_status'
data = {"payment_id": 123456,  
        "status": "COMPLETED"}

response = requests.post(url, json=data)
print(response.text)