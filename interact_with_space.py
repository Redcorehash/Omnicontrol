import requests
import json

# Define the URL for the Hugging Face Space
SPACE_URL = "https://api-inference.huggingface.co/models/Yuanshi/OminiControl"

# Define your Hugging Face API token
API_TOKEN = "your_huggingface_api_token"

def send_request(payload):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(SPACE_URL, headers=headers, data=json.dumps(payload))
    return response.json()

def main():
    # Example payload
    payload = {
        "inputs": "Hello, how are you?",
        "parameters": {
            "max_length": 50
        }
    }
    
    response = send_request(payload)
    print("Response from Hugging Face Space:")
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
