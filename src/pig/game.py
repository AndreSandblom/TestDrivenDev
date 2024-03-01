""" Game class: Single Player & 2 Players modes
    Pig game with dice roll, increment and determine winner
    and cheat etc functions """

from dice import Dice
from player import Player

class Game:
    
    def __init__(self, player1=None, player2=None):
        """Constructor for single and 2 player game."""
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

    def roll_dice(self):
        """A dice is rolled and an integer is returned."""
        return self.dice.roll()
        
    def intelligence_roll_dice(self):
        """Computer decides if or not to roll a dice and an integer is returned."""
        pass # return self.intelligence.roll()                    

    def get_score(self, player):
        """Get the current score of the player."""
        if player == self.player1.get_name():
            return self.score1
        elif player == self.player2.get_name():
            return self.score2
        else:
            raise ValueError("Invalid player.")             # Need to handle error

    def increment_and_determine(self, player, num_rolled):
        """A score adder that checks if there is a winner,
           if there is, the function returns a dictionary, else 0."""
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

    def has_won(self, score):
        """Check if a player has won."""
        if score >= self.winning_score:
            return True
        else:
            return False
    
    def winner(self):
        """Generates a dictionay of name and score."""
        if self.score1 > self.score2:
            winner_table = {self.player1.get_name(): self.score1, self.player2.get_name(): self.score2}
        else:
            winner_table = {self.player2.get_name(): self.score2, self.player1.get_name(): self.score1}
        return winner_table

    def cheat(self):
        """To set the winning score to 50 to end game faster."""
        self.winning_score = 50

    def set_score(self, num1, num2):
        """Set player scores."""
        self.score1 = num1 
        self.score2 = num2

    def get_winning_score(self):
        """Get the winnning score."""
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
try:
    print(game.get_score("A"))
except ValueError as e:
    print(e)

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

