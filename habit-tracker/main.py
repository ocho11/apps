import os
import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.environ.get("PIXELA_TOKEN")
USER_NAME = "python20230820"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_ID = "graph"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

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

graph_params = {
    "id": GRAPH_ID,
    "name": "Running",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

not_created_graph = False
if not_created_graph:
    response_graph = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
    print(response_graph.text)

today = datetime.now().strftime("%Y%m%d")
pixel_params = {
    "date": today,
    "quantity": input("How many kilometers did you run today?"),
}

not_created_pixel = False
if not_created_pixel:
    response_pixel = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
    print(response_pixel.text)

update_date = today
pixel_update_body_params = {
    "quantity": "5.5",
}

update_data = False
if update_data:
    response_update = requests.put(url=f"{PIXEL_ENDPOINT}/{today}", json=pixel_update_body_params, headers=headers)
    print(response_update.text)

delete_data = False
if delete_data:
    response_delete = requests.delete(url=f"{PIXEL_ENDPOINT}/{today}", headers=headers)
    print(response_delete.text)