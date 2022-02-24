#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
sheet_data = data.sheet_api_data

# loop through all rows returned by sheety api call in DataManager class
for x in sheet_data["prices"]:
    # run code below for each empty cell in google sheets
    if x["iataCode"] == "":
        # create an instance of FlightSearch class for each missing IATA code
        flight_search = FlightSearch(x["city"])
        missing_iata = flight_search.get_iata_code()
        data.update_iata(iata_code=missing_iata, row_id=x["id"])
    # for each row in sheet, create an instance of FlightData class
    flight_test = FlightData(aita=x["iataCode"], city=x["city"])
    # call FlightData method to fetch all flight data
    flight_test.get_flights()
    # call FlightData method to fetch the cheapest flight price to each city in sheet
    cheapest_flight = flight_test.get_cheapest_flight()
    if cheapest_flight > 5 and cheapest_flight < x["lowestPrice"]:
        notification = NotificationManager()
        message = f"for your trip to {x['city']}, the cheapest fare is: ${cheapest_flight}CAD"
        notification.send_text_notification(message)
