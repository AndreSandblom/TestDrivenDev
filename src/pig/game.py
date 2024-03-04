""" Game class: Single Player & 2 Players modes
    Pig game with dice roll, increment and determine winner
    and cheat etc functions """

from dice import Dice
from player import Player
from intelligence import Intelligence


class Game:
    """Pig game with dice roll, increment and determine winner"""
    def __init__(self, player1, player2):
        """Constructor for single and 2 player game."""
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice(6)
        self.winning_score = 100
        self.score1 = 0
        self.score2 = 0

    def roll_dice(self):
        """A dice is rolled and an integer is returned."""
        return self.dice.roll()

    def get_score_1(self):
        """Get player 1 score."""
        return self.score1

    def get_score_2(self):
        """Get player 2 score."""
        return self.score2

    def increment_and_determine_1(self, num_rolled):
        """A score adder that checks if there is a winner,
           if there is, the function returns a dictionary, else 0."""
        self.score1 += num_rolled
        if self.has_won(self.score1) is True:
            return self.winner()
        else:
            return 0

    def increment_and_determine_2(self, num_rolled):
        """A score adder that checks if there is a winner,
           if there is, the function returns a dictionary, else 0."""
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
        """Generates a dictionary of name and score."""
        if self.score1 > self.score2:
            winner_table = {
                self.player1: self.score1,
                self.player2: self.score2
            }
        else:
            winner_table = {
                self.player2: self.score2,
                self.player1: self.score1
            }
        return winner_table

    def cheat(self):
        """To set the winning score to 50 to end the game faster."""
        self.winning_score = 50

    def set_score(self, num1, num2):
        """Set player scores."""
        self.score1 = num1
        self.score2 = num2

    def get_winning_score(self):
        """Get the winnning score."""
        return self.winning_score


# ------------------------TEST------------------------#

# Print names
game = Game("Jenny", "William")
name1 = game.player1
name2 = game.player2
print(name1, name2)

# Set scores
game.set_score(30, 49)
print(game.get_score_1())
print(game.get_score_2())

# Cheat - winning score = 50
game.cheat()

# Roll dice and increment score and determine win or not
first_roll = game.roll_dice()
print("The first roll is: " + str(first_roll))
result = game.increment_and_determine_1(first_roll)
if result == 0:
    print(game.get_score_1())
else:
    print(result)

# Roll dice and increment score and determine win or not
first_roll = game.roll_dice()
print("The first roll is: " + str(first_roll))
result2 = game.increment_and_determine_2(first_roll)
if result2 == 0:
    print(game.get_score_2())
else:
    print(result2)
