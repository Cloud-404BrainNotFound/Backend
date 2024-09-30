import requests

url = 'http://localhost:8000/users/add_user'
local = 0
if local:
    url = 'http://localhost:8000/users/add_user'
else:
    url = 'http://54.83.149.21:8001/users/add_user'
data = {
    "username": "tes2t_user",
    "email": "123@example.com",
    "password": "password123",
    "role": "CUSTOMER",  # CUSTOMER or MERCHANT
    "store_id": "store123"  # 可选
}

response = requests.post(url, json=data)
print(response.text)