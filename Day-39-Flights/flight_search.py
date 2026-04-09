from decouple import config
from pprint import pprint
from datetime import datetime
import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):

        self.API_KEY = config("API_ACCESS_KEY")
    
    def get_api_flight_data(self):

        
        url = "http://api.aviationstack.com/v1/flights"

        params = {
        "access_key": self.API_KEY,
        "dep_iata": "LHR",
        "limit": 100
        }

        response = requests.get(url, params=params)
        data = response.json()

        flights = data.get("data", [])

        results = []

        for flight in flights:

            # -----------------------
            # AIRLINE DATA
            # -----------------------
            airline = flight.get("airline", {})
            airline_name = airline.get("name")
            airline_iata = airline.get("iata")

            # -----------------------
            # FLIGHT DATA
            # -----------------------
            flight_info = flight.get("flight", {})
            flight_iata = flight_info.get("iata")
            flight_number = flight_info.get("number")

            # fallback jeśli brak iata
            if not flight_iata:
                flight_iata = f"{airline_iata}{flight_number}"

            # -----------------------
            # DEPARTURE
            # -----------------------
            departure = flight.get("departure", {})
            dep_iata = departure.get("iata")
            dep_airport = departure.get("airport")

            # -----------------------
            # ARRIVAL
            # -----------------------
            arrival = flight.get("arrival", {})
            arr_iata = arrival.get("iata")
            arr_airport = arrival.get("airport")

            # -----------------------
            # STATUS + DELAY
            # -----------------------
            status = flight.get("flight_status")
            delay = arrival.get("delay")

            if delay is None:
                delay = 0

            # -----------------------
            # UNIQUE KEY
            # -----------------------
            flight_key = f"{flight_iata}-{dep_iata}-{arr_iata}"

            # -----------------------
            # TIMESTAMP
            # -----------------------
            updated_at = datetime.utcnow().isoformat()

            # -----------------------
            # FINAL RECORD
            # -----------------------
            record = {
                "flight_key": flight_key,
                "airline": airline_name,
                "flight_number": flight_number,
                "dep_iata": dep_iata,
                "arr_iata": arr_iata,
                "status": status,
                "delay": delay,
                "updated_at": updated_at
            }

            results.append(record)

        return results

