mystring = 'matthew'

l =list(mystring)
t = tuple(mystring)

l[0] = 't'

print(l)

# cannot change tuples
# t[0] = 'h'

print(t)

for letter in t:
    print(letter)