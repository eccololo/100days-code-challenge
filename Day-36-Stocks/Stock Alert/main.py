import requests
from pprint import pprint
import datetime
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_n_days_date_before(n):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_day_before_date = (date_now - delta).date()
    return str(n_day_before_date)


alpha_vantage_api_key = os.environ.get("AV_API_KEY")

alpha_vantage_request_url = 'https://www.alphavantage.co/query'
alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": alpha_vantage_api_key
}
response_stocks = requests.get(alpha_vantage_request_url, params=alpha_vantage_parameters)
data_stocks = response_stocks.json()

two_days_before = get_n_days_date_before(2)
one_day_before = get_n_days_date_before(1)

stock_close = float(data_stocks["Time Series (Daily)"][two_days_before]['4. close'])
stock_open = float(data_stocks["Time Series (Daily)"][one_day_before]['1. open'])
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

if diff >= 0.1:
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_api_params = {
        'q': COMPANY_NAME,
        'from': get_n_days_date_before(7),
        'sortBy': 'popularity',
        'apiKey': news_api_key
    }
    news_api_request_url = 'https://newsapi.org/v2/everything'

    response_news = requests.get(news_api_request_url, params=news_api_params)
    data_news = response_news.json()
    articles_3 = data_news['articles'][:3]
    for item in articles_3:
        author = item['author']
        content = item['content']
        desc = item['description']
        title = item['title']
        published_at = item['publishedAt'].split("T")[0]
        url = item['url']
        image = item['urlToImage']
        who_published = item['source']

        print(title)


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
