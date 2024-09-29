import requests

url = 'http://localhost:8000/orders/search_orders_by_user'
local = 0
if local:
    url = 'http://localhost:8000/orders/search_orders_by_user'
else:
    url = 'http://54.83.149.21:8004/orders/search_orders_by_user'
data = {"user_id": "uuid-user-1234"}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response Data:", response.json())