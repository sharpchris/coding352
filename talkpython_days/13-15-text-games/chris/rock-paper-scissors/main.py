from classes import Player, Roll
import random

def main():
    print_header()
    name = get_player_name()
    target = get_target_wins()
    player = Player(name)
    computer = Player('Computer')
    game_loop(player, computer, target)

def game_loop(player, computer, target):
    while player.score < target and computer.score < target:
        choice = input("Choose rock, paper, or scissors: ")
        if choice in ['rock','scissors','paper']:
            computer_roll = Roll(get_random_choice())
            player_roll = Roll(choice)
            print(f'The computer chose {computer_roll.choice}')
            round_state = player_roll.can_defeat(computer_roll)
            if round_state:
                print("You won!", end="\n\n")
                player.score += 1
            elif round_state == False:
                print("Sorry, you lost.", end="\n\n")
                computer.score += 1
            else:
                print("It's a tie!", end="\n\n")
            continue
        if choice == 'score':
            display_score(player, computer)
        if choice in ['exit','quit','q']:
            print("Thank you for playing!")
            break
    display_score(player, computer)
    if player.score == target:
        print("Yay, you won!")
    else:
        print("You were beaten by a thinking rock.")

def print_header():
    print("\n*** Welcome to Sharp's Rock-Paper-Scissorsro Game! ***", end = "\n\n")

def get_player_name():
    name = input("What is your name? ")
    print(f'Greetings, {name}', end='\n\n')
    return name

def get_random_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_target_wins():
    wins = input('How many wins do you want to play to? ')
    try:
        wins = int(wins)
    except:
        print("That's not an integer. Let's play to 5")
        return 5
    return wins

def display_score(player, computer):
    print('{}\'s score is {} and the computer\'s is {}'.format(player.name, player.score, computer.score))

if __name__ == "__main__":
    main()