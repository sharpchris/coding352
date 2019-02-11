>>> number = list(range(1, 11))
>>> number
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in number:
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
>>> # For loop is calling the iter __ method.
...

>>> '__iter__' in dir('number')
True

>>> it = iter('string')
>>> next(it)
's'
>>> next(it)
't'
>>> next(it)
'r'
>>> next(it)
'i'
>>> next(it)
'n'
>>> next(it)
'g'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> # Get a traceback because we are calling `next` directly.
...
>>> # A For loop expects the StopIteration and handles that

####
# Itertools Cycle
####

>>> import itertools, sys, time
>>>
>>> symbols = itertools.cycle('-\|/')
>>>
>>> while True:
...     cycle = 0
...     sys.stdout.write('\r' + next(symbols))
...     cycle += 1
...     if cycle == 100:
...             break
...     sys.stdout.flush()
...     time.sleep(.1)
...
-2
\2
|2
/2
-2
\2
|2
/2
-2
\2
|2
.....
