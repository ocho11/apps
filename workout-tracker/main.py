import requests
import os

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
RECORD_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

your_workout_info = input("Tell me which exercise you did: ")
parameters = {
    "query": your_workout_info,
}

response = requests.post(url=RECORD_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()

response_json = response.json()
print(response_json)

sheety_params = {
    "workout":
        {
            "date": "21/07/2023",
            "time": "15:00:00",
            "exercise": "Running",
            "duration": 22,
            "calories": 130,
        }
}
