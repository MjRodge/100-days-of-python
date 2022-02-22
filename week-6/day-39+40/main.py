#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheet_data = data.sheet_api_data

for x in sheet_data["prices"]:
    if x["iataCode"] == "":
        flight_search = FlightSearch(x["city"])
        print(f"i am an instance of flightsearch class, i shall search for {flight_search.city_name}")
        data.update_iata(iata_code="TESTING", row_id=x["id"])
