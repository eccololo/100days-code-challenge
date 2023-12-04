import os
import requests
import datetime


def get_current_date_and_time():
    """Returning current time and date as a tuple."""
    time = datetime.datetime.now().time().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    return date, time


def get_data_from_nutritionix_as_json(endpoint, params, heads):
    """Returning JSON data from Nutritionix API."""
    return requests.post(url=endpoint, json=params, headers=heads).json()


def get_sheety_payload_as_dict(response):
    """Creating a payload dict to send to Sheety and to Save data to Google Sheets."""
    dur_min = response["exercises"][0]["duration_min"]
    cals = response["exercises"][0]["nf_calories"]
    execs = str(response["exercises"][0]["name"]).title()
    date, time = get_current_date_and_time()

    temp_dict = {
        'Date': date,
        'Time': time,
        'Duration': dur_min,
        'Exercise': execs,
        'Calories': cals
    }

    return temp_dict


def send_data_to_google_sheets_and_return_status_code_and_text(endpoint, params):
    """Sending data to Google Sheets and returning server response status code."""
    resp = requests.post(
        url=endpoint,
        json=params,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        ))

    return resp.status_code, resp.text



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
    current_time = get_current_date_and_time()[1]
    current_date = get_current_date_and_time()[0]

    response = get_data_from_nutritionix_as_json(NUTRI_END_POINT, request_parameters, headers)

    sheety_params[GOOGLE_SHEET_NAME] = get_sheety_payload_as_dict(response)

    # FIXME:
    #    1. Data are sent but doesn't saved in Google Sheets - Why?

    success = send_data_to_google_sheets_and_return_status_code_and_text(SHEETY_ENDPOINT, sheety_params)

    if success[0] != 200:
        print("Ups. Something went wrong.")
    else:
        print("Data added to your Google Sheet successfully.")

    print("*" * 30)
    print("[Analysis]:")
    print(f"Server response status code: {success[0]}")
    print(f"Server response message: {success[1]}")
