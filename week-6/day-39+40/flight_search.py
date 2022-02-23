import requests
from datetime import datetime, timedelta
from keys import TEQUILA_API
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_AITA_QUERY = "/locations/query"
TEQUILA_LOCATION_QUERY = "/search"

headers = {
            "apikey": TEQUILA_API
        }

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.city_name = city_name
        self.today = datetime.now()
        self.six_months = self.today + timedelta(days=180)

    def get_iata_code(self):
        payload = {
            "term": self.city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_AITA_QUERY}", params=payload, headers=headers)
        response.raise_for_status()
        returned_data = response.json()["locations"]
        return returned_data[0]["code"]

    def get_flight_details(self):
        date_from = self.today.strftime("%d/%m/%Y")
        date_to = self.six_months.strftime("%d/%m/%Y")
        payload = {
            "fly_from": "YYZ",
            "fly_to": self.city_name,
            "date_from": date_from,
            "date_to": date_to,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "CAD",
            "max_stopovers": 0,
            "limit": 2
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_LOCATION_QUERY}", params=payload, headers=headers)
        response.raise_for_status()
        print(response.json()["data"])



