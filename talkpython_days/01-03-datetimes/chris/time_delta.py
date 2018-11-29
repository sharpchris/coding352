from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(t.days)
print(t.seconds)

# "t.hours" doesn't work; timedelta only stores days and
# up to 24 hours worth of seconds

print(t.seconds / 60 /60 )


eta = timedelta(hours=6)

today = datetime.today()


today + eta
# adding a timedelta to a datetime works just like you might like!

print(str(today + eta))
 