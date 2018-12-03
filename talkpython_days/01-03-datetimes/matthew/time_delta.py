from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(type(t))

eta = timedelta(hours=6)

today = datetime.today()

print(today)

print(eta)

print(today + eta)

print(str(today + eta))