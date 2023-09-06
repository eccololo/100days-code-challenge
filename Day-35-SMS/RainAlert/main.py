import requests
from twilio.rest import Client

twilio_account_sid = '<account_sid>'
twilio_auth_token = '<api_key>'
twilio_client = Client(twilio_account_sid, twilio_auth_token)

api_endpoint_standard = "https://api.openweathermap.org/data/2.5/weather"
api_key = "<api_key>"

# Krakow, PL
parameters_3_days = {
    "lat": 50.064651,
    "lon": 19.944981,
    "appid": api_key
}

parameters_standard = {
    "q": "Krakow,pl",
    "appid": api_key
}

response = requests.get(api_endpoint_standard, params=parameters_standard)
response.raise_for_status()

weather_code = response.json()['weather'][0]['id']
if weather_code <= 800:
    message = twilio_client.messages.create(
        from_='<tel_from>',
        to='<tel_to>',
        body="Please, take with you an umbrella today ☂️."
    )

    print(message.status)

