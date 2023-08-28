import requests
from datetime import datetime

MY_LAT = 50.064651
MY_LONG = 19.944981

# ISS LOCATION API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

# SUN RISE SUN SET API

# Cords for Kraków, Poland
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_hour = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset_hour = data['results']['sunset'].split("T")[1].split(":")[0]
now_datetime_hour = datetime.now().hour
print(sunrise_hour)
print(sunset_hour)
print(now_datetime_hour)