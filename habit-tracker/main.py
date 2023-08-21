import os
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.environ.get("PIXELA_TOKEN")
USER_NAME = "python20230820"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

not_created_user = False
if not_created_user:
    response_user = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response_user.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_params = {
    "id": "graph",
    "name": "Running",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response_graph = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
print(response_graph.text)

