from datetime import datetime
from datetime import date

datetime.today()

today = datetime.today()

print(type(today))

todaydate = date.today()

print(type(todaydate))

print(todaydate)

print(todaydate.month)

print(todaydate.day)

print(todaydate.year)

christmas = date(2018, 12, 25)

print(christmas)

print(christmas - todaydate)

(christmas - todaydate).days

if christmas is not today:
    print("There are " + str((christmas - todaydate).days) + " days until Christmas!")
else:
    print("It's Christmas")

