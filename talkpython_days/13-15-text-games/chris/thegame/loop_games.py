from main import play_game
from statistics import mean, median, mode
import os, sys

NUMBER_OF_GAMES = 1500
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

print(f"We are going to play {NUMBER_OF_GAMES} games. Please stand by.")
outcomes = []
with HiddenPrints():
    for _ in range(NUMBER_OF_GAMES):
        outcomes.append(play_game())

outcomes.sort()
print(f"The best game had {str(min(outcomes))} remaining.")
print(f"The worst game had {str(max(outcomes))} remaining.")
print(f"The average game had {str(mean(outcomes))} cards remaining.")
print(f"The median game had {str(median(outcomes))} cards remaining.")
try:
    print(f"The mode was {str(mode(outcomes))} cards remaining.")
except StatisticsError:
    print("There was more than one most common value, so there is no mode.")
print(outcomes)