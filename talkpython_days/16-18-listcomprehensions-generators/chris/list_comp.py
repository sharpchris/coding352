from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

names = 'pybites mike bob julian tim sara guido'.split()
print(names)

for name in names:
    # Title Case
    print(name.title())

alphabet = list(string.ascii_lowercase)
# Print whole lowercase alphabet
print(alphabet)
# Now print just the first half
first_half_alphabet = alphabet[:13]
print(first_half_alphabet)

# One method to get list of names if they start with first half of alphabet
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())

# Now best way to get list of names that start with first half of alphabet
# Using list comprehensions

new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]

assert new_names == new_names2

# Word counts with Harry Potter
resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
words = resp.text.lower().split()
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))

# Clean out non-alphabetic characters
# Will leave in empty words
words = [re.sub(r'\W+', r'', word) for word in words]

# Get "stopwords"
resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()

# Take out empty words and words that are in the list of stopwords
words = [word for word in words if word.strip() and word not in stopwords]
# Can check to see if "the" has been properly removed
assert "the" not in words

cnt = Counter(words)
print(cnt.most_common(5))