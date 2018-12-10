from datetime import datetime
from datetime import timedelta
from time import sleep

print ("Start working. I will tell you when to take a break.")

worktime = timedelta(seconds=(25*60))
now = datetime.today()
stoptime = now + worktime

while datetime.today() < stoptime:
    minutesleft = ((stoptime - datetime.today()).seconds + 1) / 60
    print ("Keep working, only " + str(minutesleft) + " minutes left!")
    sleep(60)

print ("Good job, you can take a break now.")