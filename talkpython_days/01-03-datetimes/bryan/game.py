from datetime import datetime
from datetime import date
from datetime import timedelta

today = datetime.today()
todaydate = date.today()
print(today.year)
print(todaydate)

age = input("What is your age?")

age = int(age)

agedelta = (today.year - age)
secondagedelta = (today.year - age - 1)

birthdayoccur = input("Has your birthday already passed this year?  Please respond with 'y' for yes, and 'n' for no.")

if birthdayoccur == 'y':
    print("You were born in " + str(agedelta))
else:
    print("You were born in " + str(secondagedelta))