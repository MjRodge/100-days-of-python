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
        return flight_data

    def get_cheapest_flight(self):
        flight_search = FlightSearch(self.departure_aita_code)
        flight_data = flight_search.get_flight_details()
        cheapest_flight = 0
        for x in flight_data:
            if x["price"] > cheapest_flight:
                cheapest_flight = x["price"]
        return cheapest_flight
