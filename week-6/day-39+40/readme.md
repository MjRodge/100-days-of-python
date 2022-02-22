# days 39 + 40 - flight club

## objectives
- create a program that queries an api with data around flight prices
- store a historical low flight price in google sheets
- compare this historical low price daily, to look for flights that are less than the historical value
- when a flight is found, use [twilio api](https://www.twilio.com/) to send a text message alerting user of deal

## apis used
- Google Sheet Data Management - https://sheety.co/
- Kiwi Partners Flight Search API - https://partners.kiwi.com/
- Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
- Twilio SMS API - https://www.twilio.com/docs/sms

## steps taken
1. prepare google sheet data store by copying starting spreadsheet from course material
2. link google sheet to sheety api, and enable _**put**_ permissions to allow updating of rows
3. change sheety authentication method to _**bearer token**_
4. prepare `secrets.py` and `.gitignore` for storage of secret tokens
5. sign up for kiwi flight search api
6. add tequila-api (kiwi flight search) key to `keys.py`
7. make a _**GET**_ request to sheety api, pulling in all data from google sheets document in `data_manager.py`
8. pass through sheety response data to `main.py` and save to a variable
9. check each row of data from sheety for empty `iataCode` value, replace empties with "TESTING" for now
10. should a row be empty, pass the name of the city returned by the sheety api call to `flight_search.py`
11. created a method within the `DataManager` class that sends a _**PUT**_ request to sheety api for filling in blank cells in google sheets