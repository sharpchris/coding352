from unittest.mock import patch
import random, pytest
from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_numer(m):
    # Fix the random number that is generated to make testing easier
    m.return_value = 17
    assert get_random_number() == 17

@patch("builtins.input", side_effect=[11, '12', 'bob', 12, 5, -1,21, 7, None])
def test_guess(inp):
    game = Game()
    # Good (11, '12')
    assert game.guess() == 11
    assert game.guess() == 12
    # NAN ('bob')
    with pytest.raises(ValueError):
        game.guess()
    # Already guessed 12 (12)
    with pytest.raises(ValueError):
        game.guess()
    # Good (5)
    assert game.guess() == 5
    # Out of Range (-1, 21)
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # Good (7)
    assert game.guess() == 7
    with pytest.raises(ValueError):
        game.guess()

def test_validate_guess(capfd):
    #capfd captures the standard output to test what is being printed
    game = Game()
    game._answer = 2

    # If we guess a 1 when the answer is 2, make sure that validate_guess
    # is returning False
    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'
    
    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'
    
    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'

# Simulate a whole game that ends in a win
@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range', '9 is too high', 'Already guessed', '6 is correct!', 'It took you 3 guesses']

    # splitting output, ignoring blank lines, and striping extra spaces and junk
    output = [line.strip() for line in out.split('\n') if line.strip()]
    assert output == expected

# Simulate a whole game that ends in a loss
@patch("builtins.input", side_effect=[None, 1, 2, 3, 4, 5])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    # Play the game and make sure it is recorded as a loss
    game()
    assert game._win is False

    # Test the final print statement if game is lost
    out = capfd.readouterr()[0]
    output = [line.strip() for line in out.split('\n') if line.strip()]
    expected = 'Guessed 5 times, answer was 13'
    assert output.pop() == expected