import requests
import os
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
TEN_DOLLAR = 10

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
SMS_FROM = os.environ.get("TWILIO_FROM_PHONE_NUMBER")
SMS_TO = os.environ.get("TWILIO_TO_PHONE_NUMBER")

stock_exchange_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

response_stock = requests.get(STOCK_ENDPOINT, stock_exchange_parameters)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = float(stock_data_list[0]["4. close"])
day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])

up_down = None
if yesterday_closing_price > day_before_yesterday_closing_price:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(yesterday_closing_price - day_before_yesterday_closing_price) >= TEN_DOLLAR:
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    three_articles = response_news.json()["articles"][:3]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    three_messages = [f"{COMPANY_NAME}: {up_down}\nHeadline: {article['title']}.\nBrief: {article['description']}" for
                      article in three_articles]
    for message in three_messages:
        mess = client.messages.create(
            body=message,
            from_=SMS_FROM,
            to=SMS_TO,
        )
