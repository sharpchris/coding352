def fizzbuzz(n):
    if n % 15 == 0:
        return 'Fizz Buzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    return n