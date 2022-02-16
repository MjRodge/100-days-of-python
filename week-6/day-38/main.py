import requests
from keys import NUTRITIONIX_API_KEY, NUTRITIONIX_APP_ID

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 182.64,
    "age": 30
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=params)
response.raise_for_status()

data = response.json()
print(data)
