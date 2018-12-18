from classes import Player

def main():
    print_header()
    name = get_player_name()
    player1 = Player(name)
    game_loop(player1)

def game_loop(player1):
    print (player1.name)
    exit()

def print_header():
    print("*** Welcome to Sharp's Rock-Paper-Scissors Game! ***", end = "\n\n")

def get_player_name():
    name = input("What is your name? ")
    print(f'Greetings, {name}', end='\n\n')
    return name

if __name__ == "__main__":
    main()