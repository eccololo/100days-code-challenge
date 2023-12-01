import os
import requests

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 190
AGE = 34

APP_ID = os.environ.get("NUTRITIONIX_API_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRI_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

request_parameters = {
    'query': "doing yoga for 45 minutes",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

if __name__ == "__main__":
    response = requests.post(url=NUTRI_END_POINT, json=request_parameters, headers=headers)
    print(response.text)