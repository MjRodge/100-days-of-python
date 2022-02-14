import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

date_of_birth = dt.datetime(year=1991, month=10, day=31)

print(date_of_birth)
print(f"year: {year} month: {month} day: {day}")
