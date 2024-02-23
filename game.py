# Game class: Single Player & 2 Players modes
from dice import Dice1

class Game:
    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice1
        self.score1 = 0
        self.score2 = 0
    
    # A dice is rolled and an integer is returned
    def roll_dice(self):
        num_rolled = self.dice.roll()
        return num_rolled
    
    # Computer rolls a dice and an integer is returned
    def intelligence_roll_dice(self, intelligence):
        self.intelligence = intelligence
        num_rolled = self.intelligence.roll()                    # Intelligence class rolls a dice
        return num_rolled

    # A score adder
    def add_score(self, score, num_rolled):
        self.score = score
        return self.score + num_rolled
    
    def cheat(self):
        pass
    
    def restart(self):
        pass

    def get_score_board(self):
        pass

    def get_Histogram(self):
        pass

    def set_score(self, player):
        player1.set_score()


    def quit(self):
        pass