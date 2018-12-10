from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
type(t)
t.days
t.seconds
t.seconds / 60 / 60
t.seconds / 3600

eta = timedelta(hours=6)
today = datetime.today()
today
eta
today + eta
str(today + eta)