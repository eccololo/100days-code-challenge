import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):

        self.add_endpoint = "https://api.sheety.co/d150a438f289ecabec118a7229ec2c48/flightDeals/sheet1"
        self.read_endpoint = "https://api.sheety.co/d150a438f289ecabec118a7229ec2c48/flightDeals/sheet1"
    

    def upload_flights_data(self, flights_data):

        for flight in flights_data:

            body = {
                "sheet1": {
                    "flightKey": flight["flight_key"],
                    "airline": flight["airline"],
                    "flightNumber": flight["flight_number"],
                    "depIata": flight["dep_iata"],
                    "arrIata": flight["arr_iata"],
                    "status": flight["status"],
                    "delay": flight["delay"],
                    "updatedAt": flight["updated_at"]
                }
            }

            response = requests.post(self.add_endpoint, json=body)

        if response.status_code != 201:
            print("ERROR:", response.text)
            return False
        else:
            print(response.status_code, response.text)
            return True
        

    def get_flights_from_google_sheet(self):
        response = requests.get(self.read_endpoint)
        data = response.json()
        return data["sheet1"]