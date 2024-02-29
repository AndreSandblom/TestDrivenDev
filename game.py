# Game class: Single Player & 2 Players modes
from dice import Dice
from player import Player

class Game:
    
    def __init__(self, player1=None, player2=None):
        if player1 is not None and player2 is not None:
            self.player1 = Player(player1)
            self.player2 = Player(player2)
        elif player1 is not None:
            self.player1 = Player(player1)
            # self.player2 = Intelligence()
        self.dice = Dice(6)
        self.winning_score = 100
        self.score1 = 0
        self.score2 = 0

    # A dice is rolled and an integer is returned
    def roll_dice(self):
        return self.dice.roll()
        
    # Computer decides if or not to roll a dice and an integer is returned
    def intelligence_roll_dice(self):
        pass # return self.intelligence.roll()                    

    # Get the current score of the player
    def get_score(self, player):
        if player == self.player1.get_name():
            return self.score1
        elif player == self.player2.get_name():
            return self.score2
        else:
            print("Invalid player")

    # A score adder that checks if there is a winner
    # If a winner is born, the function returns a dictionary
    def increment_and_determine(self, player, num_rolled):
        if player == self.player1.get_name():
            self.score1 += num_rolled
            if self.has_won(self.score1) is True:
                return self.winner()
            else:
                return 0
        elif player == self.player2.get_name():
            self.score2 += num_rolled
            if self.has_won(self.score2) is True:
                return self.winner()
            else:
                return 0

    # Check if a player has won
    def has_won(self, score):
        if score >= self.winning_score:
            return True
        else:
            return False
    
    # Generates a dictionay of name and score
    def winner(self):
        if self.score1 > self.score2:
            winner_table = {self.player1.get_name(): self.score1, self.player2.get_name(): self.score2}
        else:
            winner_table = {self.player2.get_name(): self.score2, self.player1.get_name(): self.score1}
        return winner_table

    # By setting the winning score to 50 to end game faster
    def cheat(self):
        self.winning_score = 50

    # To be deleted - only for testing
    def set_score(self, num1, num2):
        self.score1 = num1 
        self.score2 = num2

    def get_winning_score(self):
        return self.winning_score


#------------------------TEST------------------------#

# Print names 
game = Game("Jenny", "William")
name1 = game.player1.get_name()
name2 = game.player2.get_name()
print(name1, name2)

# Set scores
game.set_score(30, 49)
print(game.get_score(name1))
print(game.get_score(name2))

# Cheat - winning score = 50
game.cheat()

# Roll dice and increment score and determine win or not
first_roll = game.roll_dice()
print("The first roll is: " + str(first_roll))
result = game.increment_and_determine(name1, first_roll)
if  result == 0:
    print(game.get_score(name1))
else:
    print(result)

# Roll dice and increment score and determine win or not
first_roll = game.roll_dice()
print("The first roll is: " + str(first_roll))
result2 = game.increment_and_determine(name2, first_roll)
if  result2 == 0:
    print(game.get_score(name2))
else:
    print(result2)

