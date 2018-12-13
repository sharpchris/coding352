from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

user = ('bryan', 'programmer')

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user2 = User (name='brett', role='coder')

print(user2.name)

print(f'{user2.name} is a {user2.role}')

users = {'jim': 'teacher'}
users['jim']
users.get('jim')
users.get('marlene')

challenges_done = [('kyle', 5), ('jim', 10), ('marlene', 2)]

print(challenges_done)

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

words = """Hello hello hello darkness darkness my my my my my my my old old old old old old friend""".split()
print(words[:5])

print(Counter(words).most_common(5))

lst = list(range(1000000))
deq = deque(range(1000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)