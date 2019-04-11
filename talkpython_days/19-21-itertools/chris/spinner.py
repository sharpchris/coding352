import itertools, sys, time

symbols = itertools.cycle('-\|/')

while True:
    cycle = 0
    sys.stdout.write('\r' + next(symbols))
    cycle += 1
    if cycle == 100:
        break
    sys.stdout.flush()
    time.sleep(.1)