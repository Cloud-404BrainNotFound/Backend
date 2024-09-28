import requests

order_id = '97e498c1-a1eb-47f5-9601-a824fcd8ab39'
url = f'http://localhost:8000/orders/get_order/{order_id}'

response = requests.get(url)
print(response.status_code)
print(response.json())