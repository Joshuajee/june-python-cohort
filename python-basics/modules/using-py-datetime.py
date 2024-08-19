import datetime

date = datetime.datetime.now()

print(date)

print(date.year)
print(date.month)
print(date.day)
print(date.hour)


print(datetime.datetime(year=2022, month=8, day=17).date())

print(datetime.datetime.now().time())


print(date.timestamp())

date_in_the_past = datetime.datetime(year=2020, month=5, day=30, hour=12, minute=30)

print(date_in_the_past)

print(date_in_the_past.timestamp())

print(date.timestamp() - date_in_the_past.timestamp())




print(datetime.time(hour=20, minute=30))