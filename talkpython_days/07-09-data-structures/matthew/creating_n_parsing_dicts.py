proservices = {'matthew': 29, 'chris': 31, 'taylor': 26}

print(proservices)

people = {}

print(people)

people['matthew'] = 29

print(people)

people['chris'] = 103

print(people)

print(proservices.keys())
print(proservices.values())

print(proservices.items())

for keys in proservices.keys():
    print(keys)

for values in proservices.values():
    print(values)

for keys, values in proservices.items():
    print(keys + str(values))

for keys, values in proservices.items():
    print ('%s is %d years of age' % (keys, values))
