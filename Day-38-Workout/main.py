import os
import requests

APP_ID = "749076b3"
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRI_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

request_parameters = {
    'method': 'POST',
    'url': NUTRI_END_POINT,
    'headers': {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': API_KEY
    },
    'body': {
        'query': "doing yoga for 45 minutes"
    }
}

if __name__ == "__main__":
    response = requests.post(url=NUTRI_END_POINT, json=request_parameters)
    print(response.status_code)