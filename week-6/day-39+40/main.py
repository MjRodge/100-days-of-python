#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheet_data = data.sheet_api_data

# loop through all rows returned by sheety api call in DataManager class
for x in sheet_data["prices"]:
    # run code below for each empty cell in google sheets
    if x["iataCode"] == "":
        # create an instance of FlightSearch class for each missing IATA code
        flight_search = FlightSearch(x["city"])
        print(f"i am an instance of flightsearch class, i shall search for {flight_search.city_name}")
        missing_iata = flight_search.get_iata_code()
        data.update_iata(iata_code=missing_iata, row_id=x["id"])
