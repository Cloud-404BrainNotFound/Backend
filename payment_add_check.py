import requests

url = 'http://localhost:8000/payments/add_payment'
data = {
    "user_id": "123456",
    "order_id": "abc125553",
    "amount": 100.0,
    "currency": "USD",
    "status": "PENDING",# 使用枚举中的值: "PENDING", "COMPLETED", "FAILED"
    "method": "CREDIT_CARD",# 使用枚举中的值: "CREDIT_CARD", "DEBIT_CARD", "PAYPAL"
    "transaction_id": "trans001"
}
response = requests.post(url, json=data)
print(response.text)

data = {
    "user_id": "123456",
    "order_id": "abc3223",
    "amount": 100.0,
    "currency": "USD",
    "status": "PENDING",
    "method": "CREDIT_CARD",
    "transaction_id": "trans001"
}
response = requests.post(url, json=data)
print(response.text)

data = {
    "user_id": "565555",
    "order_id": "abc123",
    "amount": 100.0,
    "currency": "USD",
    "status": "PENDING",
    "method": "CREDIT_CARD",
    "transaction_id": "trans001"
}
response = requests.post(url, json=data)
print(response.text)

data = {
    "user_id": "123456",
    "order_id": "abc1213323",
    "amount": 100.0,
    "currency": "USD",
    "status": "PENDING",
    "method": "CREDIT_CARD",
    "transaction_id": "trans001"
}
response = requests.post(url, json=data)
print(response.text)

