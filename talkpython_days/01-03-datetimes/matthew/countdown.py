from datetime import date, datetime


today = date.today()
print("Today: " + today.strftime('%A, %b %d %Y'))

dob_str = input("What is your birthdate? mm/dd/yyyy --> ")

dob_data = dob_str.split("/")
dob_day = int(dob_data[1])
dob_month = int(dob_data[0])
dob_year = int(dob_data[2])
dob = date(dob_year, dob_month, dob_day)

#Calculate number of days lived
# number_of_days = (today - dob).days

#Calculate the number of days until next birthday
# this_year = today.dob_year

# next_birthday = date(this_year, dob_month, dob_day)
# if today < next_birthday:
#     gap = (next_birthday - today).days
#     print("Your birthday is in " + str(gap) + " days.")
# elif today == next_birthday:
#     print("Happy birthday, you!")
# else:
#     next_birthday = date(this_year + 1, dob_month, dob_day)
#     gap = (next_birthday - today).days
#     print("Your birthday is in " + str(gap) + " days.")