from classes import Deck, Stack, Hand

def introductions():
    print('Welcome to... The Game', end='\n\n')

def setup_game():
    # Create and shuffle the Draw deck
    deck = Deck()
    deck.shuffle()

    # Create the play stacks
    stack1 = Stack('ascending')
    stack2 = Stack('ascending')
    stack3 = Stack('descending')
    stack4 = Stack('descending')
    stacks = [stack1, stack2, stack3, stack4]

    # Create the starting hands
    hand1 = Hand()
    hand1.draw(deck)

    # While there are still cards in the deck and hand...
    while deck.cards or hand1.cards:

        # Determine how many cards MUST be played
        if deck.cards:
            requirement = 2
        else:
            requirement = 1

        plays = hand1.play(stacks, requirement)
            
        print(f"I was able to play {plays} cards")
        if plays < requirement:
            break
        hand1.draw(deck)

        for card in hand1.cards:
            print(card)

    # The game is over (didn't have enough plays)
    print('Done')

    cards_remaining = deck.size() + hand1.size()
    print(f'The Game ended with {cards_remaining} cards remaining.')
    if cards_remaining == 0:
        print("You have won The Game!!")
    elif cards_remaining < 11:
        print("You didn't win, but you did really good!")
    else:
        print("Sorry, you lost The Game. Better luck next time.")

if __name__ == "__main__":
    introductions()
    setup_game()