from datetime import datetime, timedelta
from time import sleep

print("Welcome to the Sharp Timer!")
number_minutes = input("How many minutes do you want to put on the timer? ")

# TODO: Logic to only accept <24 hours worth of seconds
time_interval = timedelta(minutes=int(number_minutes))

final_time = datetime.now() + time_interval
print("The timer will go off at " + str(final_time))

while datetime.today() < final_time:
    print("There are " + str((final_time - datetime.now()).seconds) + " seconds left on the timer.", end='\r')
    sleep(1)

print("RING RING RING! Time's up!!")
