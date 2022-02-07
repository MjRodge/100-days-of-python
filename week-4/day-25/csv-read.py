# with open("weather_data.csv") as weather:
    # data = weather.readlines()

# print(data)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["day"])

# list_temps = data["temp"].to_list()
# print(list_temps)

# temp_average = sum(list_temps) / len(list_temps)
# print(temp_average)

max_temp_num = data["temp"].max()
print(max_temp_num)

# search for data in row
monday = data[data["day"] == "Monday"]
print(monday)

# full row from max temp day
max_temp = data["temp"].max()
max_day = data[data["temp"] == max_temp]
print(max_day)