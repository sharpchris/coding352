from main import play_game
from statistics import mean, median, mode

NUMBER_OF_GAMES = 1000

outcomes = []
for _ in range(NUMBER_OF_GAMES):
    outcomes.append(play_game())

outcomes.sort()
print(f"The best game had {str(min(outcomes))} remaining.")
print(f"The average game had {str(mean(outcomes))} cards remaining.")
print(f"The median game had {str(median(outcomes))} cards remaining.")
print(f"The mode was {str(mode(outcomes))} cards remaining.")
print(outcomes)