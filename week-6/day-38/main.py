import requests
from datetime import datetime, time
from keys import NUTRITIONIX_API_KEY, NUTRITIONIX_APP_ID

# take input from user to pass to nutritionix api
# eg: "i walked 7km and ran 3km"
exercise = input("enter the activities that you did: ")

# authorisation headers for nutritionix api
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}
# parameters to pass to nutritionix api
params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 182.64,
    "age": 30
}

# send request/auth/params to nutritionix api
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=params)
response.raise_for_status()
# returned data from nutritionix api
data = response.json()
print(data)

# using python datetime to build date/time variables in correct format for submission to sheety api
date = datetime.now()
year = date.strftime("%Y")
month = date.strftime("%m")
day = date.strftime("%d")
formatted_date = f"{day}/{month}/{year}"
time = date.strftime("%H:%M:%S")

