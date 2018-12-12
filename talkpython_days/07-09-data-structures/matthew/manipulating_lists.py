numlist = [1, 2, 3, 4, 5]

print(numlist)

numlist.reverse()

print(numlist)

numlist.sort()

print(numlist)

for num in numlist:
    print(str(num))

mystring = 'matthew'

print(list(mystring))

l = list(mystring)

print(l)

print(l[0])

l.pop()

print(l)

l.insert(6, 'w')

print(l)

l[0] = 'h'

print(l)

del l[0]

print(l)

l.insert(0, 'm')

print(l)

first_letter = l.pop(0)

print(first_letter)

l.append('s')

print(l)