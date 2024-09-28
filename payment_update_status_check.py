import requests

url = 'http://localhost:8000/payments/update_status'
data = {"payment_id": 123456,  
        "status": "COMPLETED"}

response = requests.post(url, json=data)
print(response.text)