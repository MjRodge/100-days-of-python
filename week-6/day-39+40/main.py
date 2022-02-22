#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data = DataManager()
sheet_data = data.sheet_api_data

for x in sheet_data["prices"]:
    if x["iataCode"] == "":
        print(x["city"])
        x["iataCode"] = "TESTING"
    print(x["iataCode"])

# print(sheet_data)