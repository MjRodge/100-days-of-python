import requests
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

    def get_iata_code(self):
        payload = {
            "term": self.city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_AITA_QUERY}", params=payload, headers=headers)
        response.raise_for_status()
        returned_data = response.json()["locations"]
        return returned_data[0]["code"]





