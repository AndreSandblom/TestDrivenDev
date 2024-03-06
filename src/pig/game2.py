""" Game class: Single Player & 2 Players modes
    Pig game with dice roll, increment and determine winner
    and cheat etc functions """

import os
import cmd
import textwrap
import time
from dice import Dice
from intelligence import Intelligence
SCREEN_WIDTH = 60
MENU_WIDTH = SCREEN_WIDTH - 2
LEFT_PADDING = 23

DIE_SIDES = {
        1: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│         │": ^{MENU_WIDTH}}|
        |{"│    ●    │": ^{MENU_WIDTH}}|
        |{"│         │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """,
        2: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│ ●       │": ^{MENU_WIDTH}}|
        |{"│         │": ^{MENU_WIDTH}}|
        |{"│       ● │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """,
        3: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│ ●       │": ^{MENU_WIDTH}}|
        |{"│    ●    │": ^{MENU_WIDTH}}|
        |{"│       ● │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """,
        4: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"│         │": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """,
        5: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"│    ●    │": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """,
        6: f"""
        |{"┌─────────┐": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"│ ●     ● │": ^{MENU_WIDTH}}|
        |{"└─────────┘": ^{MENU_WIDTH}}|\
        """
    }


class Game(cmd.Cmd):
    """Pig game with dice roll, increment and determine winner"""

    def __init__(self, player1, player2):
        """Constructor for single and 2 player game."""
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice(6)
        self.winning_score = 100
        self.score1 = 0
        self.score2 = 0
        self.player1_turn = True
        self.player2_turn = False
        self.current_roll = 1

    prompt = "Select an option >>> "
    completekey = None

    def do_roll(self, arg):
        """Roll a dice, if it's a 1, reset turn total, the other player's turn;
        if it's not a 1, turn total increments."""
        self.current_roll = self.roll_dice()
        match(self.current_roll):
            case 1:
                self.get_current_player().turn_total = 0
                print(self.start(self.player1, self.player2))
                time.sleep(1)
                if isinstance(self.player2, Intelligence):
                    self.play_computer_turn()
                else:
                    self.change_turn()
            case _:
                self.get_current_player().turn_total += self.current_roll
      
        print(self.start(self.player1, self.player2))

    def do_hold(self, arg):
        if self.player1_turn:
            game_over = self.increment_and_determine(self.score1,
                                                     self.get_current_player()
                                                     .turn_total)
            if game_over:
                self.display_game_over(game_over)

        else:
            game_over = self.increment_and_determine(self.score2,
                                                     self.get_current_player()
                                                     .turn_total)
            if game_over:
                self.display_game_over(game_over)

        self.get_current_player().turn_total = 0

        if isinstance(self.player2, Intelligence):
            self.play_computer_turn()
        else:
            self.change_turn()
        
        print(self.start(self.player1, self.player2))
    
    def do_edit_name(self, arg):
        pass

    def do_cheat(self, arg):
        pass

    def do_restart(self, arg):
        pass

    def do_quit(self, arg):
        pass

    def clear_terminal(self):
        """Clear the terminal."""

        if os.name == 'nt':
            # For Windows
            _ = os.system('cls')
        else:
            # For Unix-like systems (macOS, Linux)
            _ = os.system('clear')

    def start(self, player1, player2):
        """Display the main screen of the game."""

        self.clear_terminal()

        die_side = DIE_SIDES[self.current_roll]
        game = textwrap.dedent(f"""
        {"-" * SCREEN_WIDTH}
        |{"PIG": ^{MENU_WIDTH}}|
        {"-" * SCREEN_WIDTH}
        |{" " * MENU_WIDTH}|
        |    Player 1: {player1.name:17}Player 2: {player2.name:17}|
        |    Score: {self.score1: <20}Score: {self.score2:<20}|
        |{" " * MENU_WIDTH}|
        |{"DIE ROLL": ^{MENU_WIDTH}}|\
        {die_side}
        |{" " * MENU_WIDTH}|
        |{self.get_current_player().name +"'s Turn": ^{MENU_WIDTH}}|
        |{"Turn Total: " + str(self.get_current_player().turn_total): ^{MENU_WIDTH}}|
        |{"roll or hold?": ^{MENU_WIDTH}}|
        |{" " * MENU_WIDTH}|
        {"-" * SCREEN_WIDTH}
        """)

        return game
  
    def get_current_player(self):
        if self.player1_turn:
            return self.player1
   
        return self.player2
    
    def change_turn(self):
        if self.player1_turn:
            self.player1_turn = False
            self.player2_turn = True
        else:
            self.player1_turn = True
            self.player2_turn = False

    def roll_dice(self):
        """A dice is rolled and an integer is returned."""
        return self.dice.roll()
    
    def play_computer_turn(self):
        self.change_turn()
        self.player2.play(self)
        self.set_score(self.score1, self.score2 + self.player2.turn_total)
        self.change_turn()

    def get_score_1(self):
        """Get player 1 score."""
        return self.score1

    def get_score_2(self):
        """Get player 2 score."""
        return self.score2

    def increment_and_determine(self, score, num_rolled):
        """A score adder that checks if there is a winner,
           if there is, the function returns a dictionary, else 0."""
        score += num_rolled
        if self.has_won(score) is True:
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
    
    def display_game_over(self, winner):
        print(winner)
        time.sleep(3)

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
