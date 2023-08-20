import os
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": "python20230820",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
