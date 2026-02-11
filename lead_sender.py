import requests


url = "https://shirinmahbuba.app.n8n.cloud/webhook-test/lead-intake"

data = {
    "message": "Hi, I am Sara from TechBD. I want to buy 10 premium licenses for our office."
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response from n8n: {response.text}")
except Exception as e:
    print(f"Error: {e}")