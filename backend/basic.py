import requests
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "Abc3", "content": "Hello world", "price": "Ds3"})

print(get_response.json())
