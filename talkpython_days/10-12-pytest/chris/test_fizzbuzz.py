import pytest

from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("arg, ret",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (15, 'Fizz Buzz'),
    (16, 16)
])

def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret

"""
def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(16) == 16
"""