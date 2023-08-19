import requests
import os
from twilio.rest import Client

weather_city = os.environ.get("WEATHER_CITY")
api_key = os.environ.get("WEATHER_API_KEY")
tomorrow_end_point = "https://api.tomorrow.io/v4/weather/forecast"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_sms_phone_number = os.environ.get("TWILIO_FROM_PHONE_NUMBER")
to_sms_phone_number = os.environ.get("TWILIO_TO_PHONE_NUMBER")

weather_parameters = {
    "location": weather_city,
    "apikey": api_key,
    "timesteps": "hourly",
}

headers = {"accept": "application/json"}
response = requests.get(tomorrow_end_point, params=weather_parameters, headers=headers)
response.raise_for_status()

weather_data = response.json()
will_rain = False
weather_data_hourly = weather_data["timelines"]["hourly"]

for weather_data_hour in weather_data_hourly[:12]:
    if weather_data_hour["values"]["weatherCode"] >= 4000:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️☔.",
        from_=from_sms_phone_number,
        to=to_sms_phone_number
    )

    print(message.status)
