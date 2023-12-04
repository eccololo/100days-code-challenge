import os
import requests
import datetime

# ===== NUTRITIONIX API =======

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 185
AGE = 34

APP_ID = os.environ.get("NUTRITIONIX_API_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRI_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

query = input("What exercise did you make?: ")

request_parameters = {
    'query': query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# ====== SHEETY API =======

SHEETY_ENDPOINT = "https://api.sheety.co/d150a438f289ecabec118a7229ec2c48/mdbMyWorkouts/workouts"

sheety_params = {
    'workouts': {
        "Date": str(),
        "Time": str(),
        "Exercise": str(),
        "Duration": int(),
        "Calories": int()
    }
}

if __name__ == "__main__":
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y/%m/%d")

    response = requests.post(url=NUTRI_END_POINT, json=request_parameters, headers=headers).json()

    duration_min = response["exercises"][0]["duration_min"]
    calories = response["exercises"][0]["nf_calories"]
    exercise = str(response["exercises"][0]["name"]).title()

    sheety_params['workouts']['Date'] = current_date
    sheety_params['workouts']['Time'] = current_time
    sheety_params['workouts']['Duration'] = duration_min
    sheety_params['workouts']['Exercise'] = exercise
    sheety_params['workouts']['Calories'] = calories