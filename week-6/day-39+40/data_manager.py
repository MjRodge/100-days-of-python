import requests
from keys import SHEETY_BEARER, SHEETY_ENDPOINT

class DataManager:
    headers = {
        "Authorization": SHEETY_BEARER
    }
    #This class is responsible for talking to the Google Sheet.
    response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
    response.raise_for_status()
    sheet_data = response.json()

    print(sheet_data)


dm = DataManager()
