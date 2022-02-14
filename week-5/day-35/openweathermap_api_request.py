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
print(response.status_code)
print(data)
