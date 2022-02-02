weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
def c_to_f(temp):
    converted_f = (temp*9/5)+32
    return converted_f


weather_f = {key: c_to_f(value) for (key, value) in weather_c.items()}

# Write your code 👇 below:


print(weather_f)
