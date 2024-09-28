import requests
from datetime import datetime

# URL for the API endpoint
url = 'http://localhost:8000/notifications/create_notification'

# Test data for creating a new notification
data = {
    "user_id": "user-uuid-1234",
    "type": "email",  # 假设 NotificationType 枚举中包含 "EMAIL"
    "content": "Welcome to our service! Thank you for signing up.",
    "sent_at": datetime.now().isoformat()  # Optional: can be None or a specific datetime
}

# Headers to indicate JSON data
headers = {
    "Content-Type": "application/json"
}

# Sending the POST request
response = requests.post(url, json=data, headers=headers)

# Printing the status code and response data
print("Status Code:", response.status_code)
print("Response Data:", response.json())