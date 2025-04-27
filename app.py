import requests

# Call the Flask API
response = requests.get("http://flask-service:5000/api/message")
if response.status_code == 200:
    print("Response from Flask API:", response.json()["message"])
else:
    print("Failed to connect to Flask API")
