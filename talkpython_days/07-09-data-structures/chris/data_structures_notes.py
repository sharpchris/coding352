## Notes for Day 7

"""
Day 7 will be video content
Day 8 is a Python Byte challenge
Day 9 will work with a dataset and dictionaries

"""

# Dictionaries are unordred

numlist = [1, 2, 3, 4, 5]
print(numlist)
numlist.reverse() # Returns None
print(numlist)
numlist.sort() # Returns None, Works on strings too
print(numlist)

for num in numlist:
    print(str(num))

mystring = 'chris'
print(mystring)
for letter in mystring:
    print(letter)

# can also chop up a string so that each char is a string in a list
print(list(mystring))

L = list(mystring)

# Can reference a position in the list
print(L[4])

L.pop() # returns the last thing from the list and removes it from that list
print(L)

L.insert(5,"s") # position 5, letter s
print(L)

L[0] = "t"
print(L)

# del to remove an item in a list
del L[0]
print(L)

print(L.pop(0))
print(L)

L.append("!!!!")
print(L)

##########################################
# Tuples
##########################################

"""
Mutability is an object that can be changed
Immutable would be something that cannot be changed
A Tuple is like a List but is immutable

"""

T = tuple(mystring)
print(T) # This prints out with () instead of [] to indicate that it is a Tuple
try:
    T[0] = "b" # This fails
except:
    print('can\'t edit a tuple')

##########################################
# Dictionaries
##########################################

"""
Dictionaries have keys and values
Uses { }
Unordered, no gurantee that they stay in the initial order
"""

pybites = {'chris': 31, 'bob': 23, 'mike': 45}
print(pybites)

# Empty dict
people = {}

# To address an item, you gotta reference a key
people['chris'] = 32
people['bob'] = 103
print(people)

"""
Interation is different from lists in that we can interact using the keys
and values seperately
"""

print(pybites.keys())
print(pybites.values())
print(pybites.items())

for value in pybites.values():
    print (value)

# To loop through both keys and values
for key, value in pybites.items():
    print(f'{key} is {value} years old') # I much prefer f strings to string formatting with % signs

    