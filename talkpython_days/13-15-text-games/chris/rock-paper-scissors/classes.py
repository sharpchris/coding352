class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def getName(self):
        return self.name

class Roll:
    def __init__(self, choice):
        self.choice = choice

    def can_defeat(self, opponent):
        if self.choice == 'rock':
            if opponent.choice == 'scissors':
                return True
            elif opponent.choice == 'paper':
                return False
            else:
                return None
        if self.choice == 'paper':
            if opponent.choice == 'rock':
                return True
            elif opponent.choice == 'scissors':
                return False
            else:
                return None
        if self.choice == 'scissors':
            if opponent.choice == 'paper':
                return True
            elif opponent.choice == 'rock':
                return False
            else:
                return None