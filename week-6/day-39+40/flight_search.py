import requests
from keys import TEQUILA_API
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_GET_QUERY = "/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.city_name = city_name

    def get_iata_code(self):
        payload = {
            "term": self.city_name,
            "location_types": "city"
        }
        headers = {
            "apikey": TEQUILA_API
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_GET_QUERY}", params=payload, headers=headers)
        response.raise_for_status()
        returned_data = response.json()["locations"]
        print(returned_data[0]["code"])


