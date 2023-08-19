import requests
import os

weather_city = os.environ.get("WEATHER_CITY")
api_key = os.environ.get("WEATHER_API_KEY")
TOMMOROW_end_point = "https://api.tomorrow.io/v4/weather/forecast"
weather_parameters = {
    "location": weather_city,
    "apikey": api_key,
    "timesteps": "hourly",
}

headers = {"accept": "application/json"}
response = requests.get(TOMMOROW_end_point, params=weather_parameters, headers=headers)
response.raise_for_status()

weather_data = response.json()
will_rain = False
weather_data_hourly = weather_data["timelines"]["hourly"]

for weather_data_hour in weather_data_hourly[:12]:
    if weather_data_hour["values"]["weatherCode"] >= 4000:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")