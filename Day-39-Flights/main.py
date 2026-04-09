#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# TODO:
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
# If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.
# The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint


if __name__ == "__main__":

    flight_search = FlightSearch()
    flight_data = flight_search.get_api_flight_data()
    data_manager = DataManager()
    is_success = data_manager.upload_flights_data(flight_data)
    sheet_flight_data = data_manager.get_flights_from_google_sheet()
    flight_data = FlightData(sheet_flight_data)
    notification_text = flight_data.get_notification_text()
    notification_manager = NotificationManager()
    is_success = notification_manager.send_notification_email(notification_text)
    
    pprint(is_success)

