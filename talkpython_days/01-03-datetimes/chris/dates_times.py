from datetime import datetime
from datetime import date

today = datetime.now()

print(type(today))

todaydate = date.today()

print(type(todaydate))

print(todaydate.month)

christmas = date(2018, 12, 25)
print(christmas)


if christmas is not todaydate:
    print("there are " + str((christmas - todaydate).days) + " days until Christmas!")
else:
    print("Woo it's Christmas!")