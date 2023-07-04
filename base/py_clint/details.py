import requests

endpoint = "http://127.0.0.1:8000/api/portfolio/18/"

project_data = {
    "title": "My Project",
    "content": "This is my project content."
}


response = requests.get(endpoint,json=project_data)
print(response.json())
print("It's Working : ",response.status_code)