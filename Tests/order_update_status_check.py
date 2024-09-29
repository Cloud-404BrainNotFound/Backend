import requests

url = 'http://localhost:8000/orders/update_order_status'
local = 0
if local:
    url = 'http://localhost:8000/orders/update_order_status'
else:
    url = 'http://54.83.149.21:8004/orders/update_order_status'


data = {
    "order_id": "97e498c1-a1eb-47f5-9601-a824fcd8ab39",
    "status": "shipped"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())