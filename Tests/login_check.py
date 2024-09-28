import requests

url = 'http://localhost:8000/users/login'
data = {
    'username': 'test_user',
    'password': 'password123'
}

response = requests.post(url, data=data)
print(response.text)