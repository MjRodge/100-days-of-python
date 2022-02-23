from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, aita, city):
        self.departure_aita_code = aita
        self.price = ""
        self.departure_city = city

    def get_flights(self):
        flight_search = FlightSearch(self.departure_aita_code)
        flight_data = flight_search.get_flight_details()
        print(flight_data)
