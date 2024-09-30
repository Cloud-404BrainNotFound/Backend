import requests

local = 0
if local:
    url = 'http://localhost:8000/users/login'
else:
    url = 'http://54.83.149.21:8001/users/login'

data = {
    'username': 'test_user',
    'password': 'password123'
}

response = requests.post(url, data=data)
print(response.text)