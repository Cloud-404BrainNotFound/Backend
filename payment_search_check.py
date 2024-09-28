import requests

url = 'http://localhost:8000/payments/search'
data = {"user_id": "123456"}
response = requests.post(url, json=data)
print(response.text)