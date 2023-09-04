import requests

api_endpoint_standard = "https://api.openweathermap.org/data/2.5/weather"
api_key = ""

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
if weather_code < 700:
    print("Please, take with you an umbrella.")

