# Game class: Single Player & 2 Players modes
from dice import Dice1

class Game:
    def __init__(self, player1=None, player2=None):
        if player1 is not None and player2 is not None:
            self.player1 = player1
            self.player2 = player2
        elif player1 is not None:
            self.player1 = player1
            # self.player2 = Intelligence()
        self.dice = Dice1()
        self.winning_score = 100
        self.score1 = 0
        self.score2 = 0

    # A dice is rolled and an integer is returned
    def roll_dice(self):
        return self.dice.roll()
        
    # Computer decides if or not to roll a dice and an integer is returned
    def intelligence_roll_dice(self):
        return self.intelligence.roll()                    

    # Get the current score of the player
    def get_score(self, player):
        if player == self.player1:
            return self.score1
        elif player == self.player2:
            return self.score2
        else:
            print("Invalid player") 

    # A score adder
    def increment_score(self, score, num_rolled):
        if self.has_won(score) is False:
            return score + num_rolled
        else:
            self.winner()

    # Check if a player has won
    def has_won(self, score):
        if score >= self.winning_score:
            return True
        else:
            return False
    
    # Generates a dictionay of name and score
    def winner(self):
        winner_table = {self.player1.get_name(): self.score1, self.player2.get_name(): self.score2}
        return winner_table

    # By setting the winning score to 50 to end game faster
    def cheat(self):
        self.winning_score = 50


    def set_score(self, num1, num2):
        self.score1 = num1 
        self.score2 = num2 



game = Game("A", "B")
game.set_score(50, 99)
print(game.get_score("A"))
print(game.get_score("B"))
first_roll = game.roll_dice()
print(game.increment_score(game.get_score("A"), game.roll_dice()))
print(game.get_score("A"))
first_roll = game.roll_dice()
print(game.increment_score(game.get_score("B"), first_roll))
print(game.get_score("B"))

