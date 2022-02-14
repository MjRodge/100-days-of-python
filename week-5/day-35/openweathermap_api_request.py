import requests

params = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": "bceee3662e28f2a0f6808b28136405bd",
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()
# print(data)

hourly_forecast = data["hourly"]
for x in range(0, 12):
    if hourly_forecast[x]["weather"][0]["id"] < 700:
        print("rain, bring an umbrella")
