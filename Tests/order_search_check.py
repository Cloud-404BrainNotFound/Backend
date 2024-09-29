import requests

order_id = '97e498c1-a1eb-47f5-9601-a824fcd8ab39'

local = 0
if local:
    url = f'http://localhost:8000/orders/get_order/{order_id}'
else:
    url = f'http://54.83.149.21:8004/orders/get_order/{order_id}'


response = requests.get(url)
print(response.status_code)
print(response.json())