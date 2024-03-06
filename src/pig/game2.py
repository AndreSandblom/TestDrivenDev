""" Game class: Single Player & 2 Players modes
    Pig game with dice roll, increment and determine winner
    and cheat etc functions """

import os
import cmd
import textwrap
import time
from dice import Dice
from highscore import Highscore
from intelligence import Intelligence
from player import Player
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
        self.current_roll = 1

    prompt = """Type a valid command or 'help' to see the existing commands.
            Select an option >>> """
    completekey = None

    def do_roll(self, arg):
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
            self.check_end_of_game(self.score1)
        else:
            self.check_end_of_game(self.score2)
    
    def do_edit_name(self, arg):
        pass

    def do_cheat(self, arg):
        self.cheat()
        if self.player1_turn:
            self.check_end_of_game(self.score1)
        else:
            self.check_end_of_game(self.score2)

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
        |{"roll OR hold": ^{MENU_WIDTH}}|
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
        else:
            self.player1_turn = True

    def roll_dice(self):
        """A dice is rolled and an integer is returned."""
        return self.dice.roll()
    
    def play_computer_turn(self):
        self.change_turn()
        self.player2.play(self)
        self.check_end_of_game(self.score2)

    def get_score_1(self):
        """Get player 1 score."""
        return self.score1

    def get_score_2(self):
        """Get player 2 score."""
        return self.score2

    def increment_and_determine(self, score, turn_total):
        """A score adder that checks if there is a winner,
           if there is, the function returns True, else False."""
        score += turn_total
        self.set_score(score)

        game_over = self.has_won(score)
        return game_over

    def has_won(self, score):
        """Check if a player has won."""
        if score >= self.winning_score:
            return True

        return False

    def winner(self):
        """Generates a dictionary of a winner and score."""
        if self.score1 > self.score2:
            winner_table = {
                "winner": self.player1,
                "score": self.score1
                }
        else:
            winner_table = {
                "winner": self.player2,
                "score": self.score2
                }
        return winner_table

    def get_winner(self, score):
        game_over = self.increment_and_determine(score,
                                                 self.get_current_player()
                                                 .turn_total)
        if game_over:
            winner_table = self.winner()
        else:
            winner_table = {}

        return winner_table
    
    def check_end_of_game(self, score):
        winner_table = self.get_winner(score)

        if winner_table:
            # resetting all values
            self.score1 = 0
            self.score2 = 0
            # save highscore
            self.update_highscores(winner_table["winner"])
            self.display_game_over(winner_table["winner"], winner_table["score"])
        else:
            self.get_current_player().turn_total = 0

            if isinstance(self.player2, Intelligence) and not isinstance(self.get_current_player(), Intelligence):
                self.play_computer_turn()
            else:
                self.change_turn()
            
            print(self.start(self.player1, self.player2))

    def display_game_over(self, winner, score):
        self.clear_terminal()
        empty_line = f"|{' ' * MENU_WIDTH}|\n"
        print()
        print("-" * SCREEN_WIDTH)
        print(f"|{'GAME OVER': ^{MENU_WIDTH}}|")
        print("-" * SCREEN_WIDTH)
        print(empty_line * 6, end='')
        print(f"|{f'{winner.name} WON': ^{MENU_WIDTH}}|")
        print(f"|{f'WITH {score} POINTS': ^{MENU_WIDTH}}|")
        print(empty_line * 4, end='')
        print(f"|{'restart OR quit': ^{MENU_WIDTH}}|")
        print(empty_line)
        print("-" * SCREEN_WIDTH)

    def update_highscores(self, winner):
        hs = Highscore("highscore.pkl2")
        players = hs.load_highscore()
        names = {player.get_name() for player in players}
        current_names = [self.player1.get_name(), self.player2.get_name()]

        for name in current_names:
            if name in names:
                for player in players:
                    if player.get_name() == name:
                        player.add_game()
                        if player.get_name() == winner.get_name():
                            player.add_win()
            else:
                new_player = Player(name)
                new_player.add_game()
                if name == winner.get_name():
                    new_player.add_win()
                players.append(new_player)

        hs.save_highscore(players)

    def cheat(self):
        """Add 50 to the current player's score to end the game faster."""
        if self.player1_turn:
            self.score1 += 50
        else:
            self.score2 += 50

    def set_score(self, score):
        """Set player scores."""
        if self.player1_turn:
            self.score1 = score
        else:
            self.score2 = score

    def get_winning_score(self):
        """Get the winnning score."""
        return self.winning_score
