from collections import Counter
from pprint import pprint
import calendar
import itertools
import random
import re
import string
import timeit

import requests


# Generators create an iterator. Then you can pluck off 
# new values from this iterator using the "yield" keyword

def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

print(next(gen), end="\n\n")

for number in gen:
    print(number)

# Generators can be used to build up something.
# Let's say we want to spit out a list of option fields
options = 'red yellow blue white black green purple'.split()

# Old Code:
def create_select_options(options=options):
    select_list = []
    
    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')
    
    return select_list

pprint(create_select_options())
print("######")

# With Generator:
def create_select_options_gen(options=options):    
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'

# Give next option
print(next(create_select_options_gen()))
# Can also assign the values to a list
all_options = list(create_select_options_gen())
print(all_options)

# Generators allow you to minimize memory needed if you don't need the whole list at once
# Compare performance of printing out all leap years:
# list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year

##
# I didn't figure out how to get timeit to work in here
# Spoiler alert: the generator method is much faster with big datasets
