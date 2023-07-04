import requests

endpoint = "http://127.0.0.1:8000/api/portfolio/create/"

data = {
    "title" : "Welcome to angular project!",
    "content" : "Thanks for visit",
    "repository":"www.github.com"
}

response = requests.post(endpoint,json=data)
# print(response.json())
print("It's Working : ",response.status_code)