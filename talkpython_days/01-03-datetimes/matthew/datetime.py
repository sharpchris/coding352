from datetime import datetime
from datetime import date

datetime.today()

today = datetime.today()
type(today)

todaydate = date.today()

type(todaydate)

todaydate

todaydate.month

todaydate.day

todaydate.year

christmas = date(2018, 12, 25)

christmas

christmas - todaydate

(christmas - todaydate).days

if christmas is not today:
    print("There are " +str((christmas - todaydate).days) + " until Christmas!")
else:
    print("It's Christmas")
