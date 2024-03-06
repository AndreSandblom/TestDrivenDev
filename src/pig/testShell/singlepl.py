""" Game class: Single player mode.

Pig game with dice roll, increment, determine winner and cheat functions.
"""
from dice import Dice
from player import Player
from highscore import Highscore
from intelligence import Intelligence
import cmd


class SingleGame(cmd.Cmd):
    """Pig game with dice roll, increment and determine winner."""

    intro = "Welcome to the game!"

    def __init__(self, difficulty):
        """Initiate constructor for single and 2 player game."""
        super().__init__()
        self.player1 = Player(1)
        self.computer = Intelligence(difficulty)
        self.dice = Dice(6)
        self.hsb = Highscore("singleGame.bin")
        self.winning_score = 100
        self.score1 = 0
        self.score2 = 0
        self.num_rolled_1 = 0
        self.num_rolled_2 = 0
        self.whose_turn = 1

    def do_set_name(self):
        """Type "set_name" to change your name from default."""
        name = input("Your new name: ")
        self.player1.change_name(name)

    def do_roll(self):
        """Type in "roll" to roll a dice."""
        if self.whose_turn == 1:
            self.num_rolled_1 = self.dice.roll()
        elif self.whose_turn == 2:
            self.num_rolled_2 = self.computer.play()            # to be modified

    def do_hold(self):
        """Type in "hold" to move to the next step."""
        if self.whose_turn == 1:
            self.increment_and_determine_1(self.num_rolled_1)
            self.whose_turn = 2
            print(f"Now is {self.player2}'s turn.")
        elif self.whose_turn == 2:
            self.whose_turn = 1
            print(f"Now is {self.player1}'s turn.")

    def do_cheat(self):
        """To set the winning score to 50 to end the game faster."""
        self.winning_score = 50
        print("Cheater... Your winning score is now set to 50!")

    def increment_and_determine_1(self, num_rolled):
        """Add score and check for winner and returns a dictionary, else 0."""
        self.score1 += num_rolled
        if self.has_won(self.score1) is True:
            return self.winner()
        else:
            return 0

    def increment_and_determine_2(self, num_rolled):
        """Add score and check for winner and returns a dictionary, else 0."""
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
        """Generate a dictionary of name and score."""
        if self.score1 > self.score2:
            print(f"Winner is: {self.player1} with {self.score1}\
                  Loser is: {self.player2} with {self.score2}")
            self.player1.add_game()
            self.player1.add_win()
        else:
            print(f"Winner is: {self.player2} with {self.score2}\
                  Loser is: {self.player1} with {self.score1}")
            self.player1.add_game()
            self.player1.add_win()
        self.hsb.save_highscore(list(self.player1,self.player2))
        self.do_exit()

    def do_exit(self):
        """Type "exit" to leave game."""
        return True
        
    def do_restart(self):
        """Type "restart" to start a new Single game."""
        print("Game restarts in 3, 2, 1...")
        self.__init__()

    def set_score(self, num1, num2):
        """Set player scores."""
        self.score1 = num1
        self.score2 = num2

    def get_winning_score(self):
        """Get the winnning score."""
        return self.winning_score
    
    def get_score_1(self):
        """Get player 1 score."""
        return self.score1

    def get_score_2(self):
        """Get player 2 score."""
        return self.score2


# ------------------------TEST------------------------#

# # Print names
# game = MultiGame("Jenny", "William")
# name1 = game.player1
# name2 = game.player2
# print(name1, name2)

# # Set scores
# game.set_score(30, 49)
# print(game.get_score_1())
# print(game.get_score_2())

# # Cheat - winning score = 50
# game.cheat()

# # Roll dice and increment score and determine win or not
# first_roll = game.roll_dice()
# print("The first roll is: " + str(first_roll))
# result = game.increment_and_determine_1(first_roll)
# if result == 0:
#     print(game.get_score_1())
# else:
#     print(result)

# # Roll dice and increment score and determine win or not
# first_roll = game.roll_dice()
# print("The first roll is: " + str(first_roll))
# result2 = game.increment_and_determine_2(first_roll)
# if result2 == 0:
#     print(game.get_score_2())
# else:
#     print(result2)
