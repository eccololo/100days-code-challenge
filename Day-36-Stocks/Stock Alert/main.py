import requests
import smtplib
from pprint import pprint
import datetime
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_IMAGE = "./images/stock-alert.jpg"
EMAIL_TO = "mateusz.hyla.it@gmail.com"
EMAIL_FROM = "mateusz.hyla.ff@gmail.com"


def get_n_days_date_before_excluding_weekends(n):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_day_before_day = (date_now - delta).date().weekday()
    n_day_before_date = (date_now - delta).date()

    # for weekends
    if n == 1:
        # if is saturday
        if n_day_before_day == 5:
            n += 1
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
        elif n_day_before_day == 6:
            n += 2
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
    elif n == 2:
        # if is sunday
        if n_day_before_day == 5:
            n += 2
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
        elif n_day_before_day == 6:
            n += 3
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()

    return str(n_day_before_date)


def get_n_days_date_before(n):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_day_before_date = (date_now - delta).date()
    return str(n_day_before_date)


def send_email_alert_about_stock(email_to, email_from, subject, message_text, message_html, app_pass):
    """This function sends email in HTML format with birthday card as attachment."""
    msg = MIMEMultipart('alternative')
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    try:
        with open(STOCK_IMAGE, 'rb') as f:
            img_data = f.read()
    except FileNotFoundError as err_msg:
        print("Image file was not found.")
        print(f"Error message: {err_msg}")
    else:
        image_send = MIMEImage(img_data, name="Stock Alert!")
        image_send.add_header('Content-ID', '<image1>')
        msg.attach(image_send)

    message = message_text
    html = message_html

    part1 = MIMEText(message, 'plain', 'utf-8')
    part2 = MIMEText(html, 'html', 'utf-8')

    msg.attach(part1)
    msg.attach(part2)

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=email_from, password=app_pass)
            conn.sendmail(from_addr=email_from,
                          to_addrs=email_to,
                          msg=msg.as_string())

    except smtplib.SMTPConnectError as err_msg:
        print(f"Error message: {err_msg}")
        return False
    else:
        return True


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

two_days_before = get_n_days_date_before_excluding_weekends(2)
one_day_before = get_n_days_date_before_excluding_weekends(1)
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
    message_txt = ""
    message_html = ""
    for item in articles_3:
        author = item['author']
        content = item['content']
        desc = item['description']
        title = item['title']
        published_at = item['publishedAt'].split("T")[0]
        url = item['url']
        image = item['urlToImage']
        who_published = item['source']['name']

        message_html += f"""
        <html>
            <head></head>
            <body>
                </br>
                <h3>{title}</h3>
                <p>Author: {author}</p>
                <p>Source: {who_published}</p>
                <p>Date: {published_at}</p>
                <p>Stock: TSLA{progress_symbol}{round(diff, 2)}%</p>
                <p>Link: <a href='{url}'>Link to article</a></p>
                <p>Image: <a href='{image}'>Link to image</a></p>
                </br>
                </br>
                <p>{content[:130]} ...</p>
                <p><img src="cid:image1"></p>
                <p style='font-weight: bold;'>{"-" * 45}</p>
            </body>
        </html>
        """

        message_txt += f"""
        Title: {title}
        Author: {author}
        Source: {who_published}
        Date: {published_at}
        Stock: TSLA{progress_symbol}{diff}%
        Link: {url}
        Image: {image}
        Content: {content}
        ----------------------------------------------
        """
    else:
        subject = f"[{COMPANY_NAME} Stock Alert] - 3 New Articles."
        email_app_pass = os.environ.get("EMAIL_APP_PASS")
        if send_email_alert_about_stock(EMAIL_TO, EMAIL_FROM, subject, message_txt, message_html, email_app_pass):
            print(f"Stock email alert sent successfuly.")
        else:
            print(f"Email not sent. Something went wrong with sending email.")
