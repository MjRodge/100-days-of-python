import requests
from keys import SHEETY_BEARER, SHEETY_ENDPOINT

headers = {
        "Authorization": SHEETY_BEARER
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
    response.raise_for_status()
    sheet_api_data = response.json()

    def update_iata(self, iata_code, row_id):
        print(f"submitting: {iata_code}, for row: {row_id}")
        sheety_payload = {
            "price": {
                "iataCode": iata_code
            }
        }
        request = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=sheety_payload, headers=headers)
        print(request.json)


