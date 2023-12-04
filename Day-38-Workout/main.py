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

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
GOOGLE_SHEET_NAME = "workout"

sheety_params = {
    GOOGLE_SHEET_NAME: {
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

    sheety_params[GOOGLE_SHEET_NAME]['Date'] = current_date
    sheety_params[GOOGLE_SHEET_NAME]['Time'] = current_time
    sheety_params[GOOGLE_SHEET_NAME]['Duration'] = duration_min
    sheety_params[GOOGLE_SHEET_NAME]['Exercise'] = exercise
    sheety_params[GOOGLE_SHEET_NAME]['Calories'] = calories

    # FIXME:
    #    1. Data are sent but doesn't saved in Google Sheets - Why?

    response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheety_params,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        ))

    if response.status_code != 200:
        print("Ups. Something went wrong.")
        print(response.status_code, response.text)
    else:
        print("Data added to your Google Sheet successfully.")
        print(response.status_code, response.text)