#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data = DataManager()
sheet_data = data.sheet_api_data

print(sheet_data)