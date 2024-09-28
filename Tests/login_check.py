import requests

url = 'http://localhost:8000/users/login'
data = {
    'username': 'test_user',
    'password': 'hashed_password'
}

response = requests.post(url, data=data)
print(response.text)