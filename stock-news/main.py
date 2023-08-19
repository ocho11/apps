import requests

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_exchange_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": "EK34XYQHLN48Q4EX",
}

response = requests.get(STOCK_ENDPOINT, stock_exchange_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = float(stock_data_list[0]["4. close"])
day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])

if abs(yesterday_closing_price - day_before_yesterday_closing_price) >= 10:
    print("Get News")