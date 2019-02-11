import itertools, time

light_sequence = itertools.cycle(['green','yellow','red'])

try:
    while True:
        light = next(light_sequence)
        print(light + "         ", end='\r')
        if light == 'green':
            time.sleep(5)
        elif light == 'yellow':
            time.sleep(1)
        else:
            time.sleep(3)
except KeyboardInterrupt:
    print("Done with the traffic light game.")
    