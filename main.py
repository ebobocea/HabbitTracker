import os
import requests
from datetime import datetime

USERNAME = os.environ['username']

TOKEN = os.environ['token']

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Programming Practice",
    "unit": "hr",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)
today = datetime.now()

pixel_update_endpoint = f"{graph_endpoint}/{graph_configuration['id']}/{today.strftime('%Y%m%d')}"

pixel_configuration = {
    "quantity": "1"
}

response = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_configuration)
print(response.text)