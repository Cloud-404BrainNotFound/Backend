import requests

url = 'http://localhost:8000/orders/search_orders_by_user'
data = {"user_id": "uuid-user-1234"}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response Data:", response.json())