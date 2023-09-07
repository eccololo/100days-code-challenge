import requests
from pprint import pprint
import datetime
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_n_days_date_before(n):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_day_before_date = (date_now - delta).date()
    return str(n_day_before_date)


alpha_vantage_api_key = os.environ.get("AV_API_KEY")
alpha_vantage_request_url = 'https://www.alphavantage.co/query'
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": alpha_vantage_api_key
}
response = requests.get(alpha_vantage_request_url, params=parameters)
data = response.json()

two_days_before = get_n_days_date_before(2)
one_day_before = get_n_days_date_before(1)

stock_close = float(data["Time Series (Daily)"][two_days_before]['4. close'])
stock_open = float(data["Time Series (Daily)"][one_day_before]['1. open'])
progress_symbols = ("🔺", "🔻")
progress_symbol = ""
if stock_open > stock_close:
    diff = 100 - (stock_close * 100) / stock_open
    progress_symbol = progress_symbols[0]
elif stock_open < stock_close:
    diff = 100 - (stock_open * 100) / stock_close
    progress_symbol = progress_symbols[1]
else:
    diff = "No difference"

# TESTING:
# print(f"Difference between yesterday and day before yesterday : {progress_symbol}{round(diff, 2)}%")

if diff >= 5.0:
    print("Get news.")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
