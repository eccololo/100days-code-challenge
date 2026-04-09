class FlightData:
    #This class is responsible for structuring the flight data.
    

    def __init__(self, sheet_flight_data):
        
        self.sheet_flight_data = sheet_flight_data


    def get_notification_text(self):

        notification = ""

        for flight in self.sheet_flight_data:

            delay = flight.get("delay") or 0

            # 1. LANDING EVENT
            if flight["status"] == "landed":
                notification += f"🛬 Lot {flight['flightNumber']} do {flight['arrIata']} właśnie wylądował.\n"
                continue  # landing ma priorytet

            # 2. DELAY SEVERITY
            if delay >= 60:
                notification += f"🔴 CRITICAL: {flight['flightNumber']} delayed {delay} min.\n"

            elif delay >= 30:
                notification += f"🟡 WARNING: {flight['flightNumber']} delayed {delay} min.\n"

            elif delay >= 15:
                notification += f"🔵 INFO: Lot {flight['flightNumber']} do {flight['arrIata']} opóźniony o {delay} min.\n"

        return notification if notification else None