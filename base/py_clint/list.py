import requests

endpoint = "http://127.0.0.1:8000/api/portfolio/create/"



response = requests.get(endpoint)
print(response.json())
print("It's Working : ",response.status_code)