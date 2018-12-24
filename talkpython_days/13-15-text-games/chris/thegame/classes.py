import random
from itertools import product
from operator import itemgetter

HAND_SIZE = 8
DIFFERENCE_TOLERANCE = 4

class Deck:
    def __init__(self):
        self.cards = list(range(2,100))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        # Check to see if we are out of cards
        if self.cards:
            return self.cards.pop()
        return None

    def size(self):
        return len(self.cards)

class Stack:
    def __init__(self, direction):
        self.direction = direction
        if direction == 'ascending':
            self.state = 1
        else:
            self.state = 100
    
    def play(self, card):
        self.state = card

    def get_state(self):
        return self.state

    def get_rollback_number(self):
        if self.direction == 'ascending':
            return self.state - 10
        else:
            return self.state + 10

class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck):
        while len(self.cards) < HAND_SIZE:
            card = deck.draw()
            # Check to see if we were able to draw
            if card:
                print(f"I drew a {card}")
                self.cards.append(card)
            else:
                break
            

    def size(self):
        return len(self.cards)

    def cards_as_str(self):
        return [str(card) for card in self.cards]
    
    def play(self, stacks, requirement):
        plays = 0
        while plays < requirement and self.cards:
            # First check to see if we can roll back any stacks
            # TODO: check to see if we can chain rollbacks
            if self.check_for_rollback_option(stacks):
                plays += 1

            # If we are already done, then stop
            if plays >= requirement:
                break

            # Get a list of tuples of the possible plays
            # Tuple structure is (card in hand, value of stack state, and difference)
            # The list of tuples is sorted based on ascending order of differences
            possible_plays = self.get_possible_plays(stacks)

            # If we have no plays, return the number of plays we made
            if not possible_plays:
                return plays

            # Play the best option
            self.make_a_play(possible_plays.pop(0), stacks)
            plays += 1

            # Check for rollback option
            if self.check_for_rollback_option(stacks):
                plays += 1

        # Now let's see if we have any good opportunities to get more cards in
        while True:
            possible_plays = self.get_possible_plays(stacks)

            # If we have no plays, return the number of plays we made
            if not possible_plays:
                return plays

            # Don't play if the extra card would cost more than the tolerance
            if possible_plays[0][2] > DIFFERENCE_TOLERANCE:
                break

            # Play the best option
            self.make_a_play(possible_plays.pop(0), stacks)
            plays += 1

            # Check for rollback option
            if self.check_for_rollback_option(stacks):
                plays += 1

        return plays

    # Given an array of stacks, return the stack with the target number
    def get_matching_stack(self, stacks, target):
        for stack in stacks:
            if stack.state == target:
                return stack
        return None

    def check_for_rollback_option(self, stacks):
        for stack in stacks:
            rollback_number = stack.get_rollback_number()
            if rollback_number in self.cards:
                print("I can roll this thing back!")
                card_to_play = self.cards.index(rollback_number)
                print(f"I'm playing {self.cards[card_to_play]} on the {stack.state}")
                stack.play(self.cards.pop(card_to_play))
                return True
        return False

    def get_possible_plays(self, stacks):
            # Get a list of stack states with directions
            states = []
            for stack in stacks:
                option = (stack.state, stack.direction)
                states.append(option)

            # Then find the lowest differences
            combinations = product(self.cards, states)
            possible_plays = []
            for option in combinations:
                if option[1][1] == 'ascending':
                    # Evaluate the difference in numbers
                    difference = option[0] - option[1][0]
                    # If it is a valid play:
                    if difference > 0:
                        possible_plays.append((option[0],option[1][0],difference))
                else:
                    # Evaluate the difference in numbers
                    difference = option[1][0] - option[0]
                    # If it is a valid play:
                    if difference > 0:
                        possible_plays.append((option[0],option[1][0],difference))
            # Sort based on the difference in numbers for the play
            possible_plays.sort(key=itemgetter(2))
            print("The possible plays are...")
            print(possible_plays)
            return possible_plays

    # play_to_make is a tuple with the format (card # to play, state # of the desired stack, difference)
    def make_a_play(self, play_to_make, stacks):
        card_to_play = self.cards.index(play_to_make[0])
        stack_to_play = self.get_matching_stack(stacks, play_to_make[1])
        print(f"I'm playing {self.cards[card_to_play]} on the {stack_to_play.state}")
        stack_to_play.play(self.cards.pop(card_to_play))
        return True