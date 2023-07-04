import requests

project_id = input("Enter project id what you want to delete  : \n")

try:
    project_id = int(project_id)
except:
    project_id = None
    print(f'{project_id} not a valid id')


if project_id:

    endpoint = f"http://127.0.0.1:8000/api/portfolio/{project_id}/delete"


    response = requests.delete(endpoint)
    print("It's Working : ",response.status_code)