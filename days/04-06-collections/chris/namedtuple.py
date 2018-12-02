from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

# namedtubple is a convenient way to define a class without methods
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')

print(user.name)
#bob

print(f'{user.name} is a {user.role}')

######
# Default Dict
######

# Dictionaries throw a key error if the value you are looking for is not there
# You can avoid this by using a dictionary's "get" method, which
# returns "None" if the key is not present
# example:

users = {'bob': 'coder'}

print(users.get('bob'))
print(users.get('julian')) # doesn't error out, retuns None
# users.julian would throw a KeyErros
# probably best to just use the get method everytime?

# building up a collection:

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]

# Using a regular dict:
#challenges = {}
#for name, challenge in challenges_done:
#    challenges[name].append(challenge)
# this errors out

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)
# so the above makes lists of the attributes that you are trying to append.

#####
# Counters
#####

# Given the text that is split up by spaces:

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5]) # print the first 5 words

# Now count the most common words, and display the five most frequent
# words and order them by frequency

# This could be done with:

common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k ,v)

# But is much easier if done with Counter!

print(Counter(words).most_common(5)) # has same effect

# In summary, Counter is a cool built in thing that should be explored
# to see what other methods it has

#####
# Deque
#####

# Pronounced "deck"

# Lists are great, but get slow when you have to reorder things
# such as when you "insert" or "delete"

# Let's make a big list and deque:

lst = list(range(10000000))
deq = deque(range(10000000))

# function to randomly remove and insert a random item
def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index,index)

# %timeit is an ipython magic function (might not work for me?)

# %timeit insert_and_delete(lst)

# summary is that it is expensive to do things with both sides of a list,
# but deques work quickly when you need to do something to both sides
# of collection

