import requests

local = 0
if local:
    url = 'http://localhost:8000/orders/add_order'
else:
    url = 'http://54.83.149.21:8004/orders/add_order'

data = {
    "user_id": "uuid-user-1234",
    "store_id": "uuid-store-5678",
    "total_amount": 99.99,
    "shipping_address": "123 Test St, Test City",
    "billing_address": "123 Test St, Test City",
    "notes": "Please deliver between 9 am and 12 pm."
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())