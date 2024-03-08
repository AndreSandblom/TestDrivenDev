"""This module contains the Mode Menu class."""
import os
import cmd
import textwrap
from difficulty_menu import DifficultyMenu
from player import Player
# from game import Game
from game2 import Game
SCREEN_WIDTH = 60
MENU_WIDTH = SCREEN_WIDTH - 2
LEFT_PADDING = 20


class ModeMenu(cmd.Cmd):
    """The mode menu for the game."""
    def __init__(self, main_menu, exit_menu):
        super().__init__()
        self.main_menu = main_menu
        self.exit_menu = exit_menu

    prompt = textwrap.dedent("""\
        Type a valid command or 'help' to see the existing commands.
        >>> """)

    def do_one(self, arg):
        """Start a single player game."""
        difficulty = DifficultyMenu(self.display_mode_menu(), self.exit_menu)
        difficulty.cmdloop(difficulty.display_difficulty_menu())

    def do_two(self, arg):
        """Start a two player game."""
        player1 = Player(input("Enter the name for Player 1 >>> ")
                         .capitalize())
        player2 = Player(input("Enter the name for Player 2 >>> ").
                         capitalize())

        game = Game(player1, player2, self.exit_menu)
        game.cmdloop(game.start(player1, player2))

    def do_back(self, arg):
        """Go back to the main menu."""
        self.clear_terminal()
        print(self.main_menu)
        return True, arg

    def clear_terminal(self):
        """Clear the terminal."""

        if os.name == 'nt':
            # For Windows
            _ = os.system('cls')
        else:
            # For Unix-like systems (macOS, Linux)
            _ = os.system('clear')

    def display_mode_menu(self):
        """Display the game mode menu."""
        self.clear_terminal()

        mode_menu = textwrap.dedent(f"""
        {"-" * SCREEN_WIDTH}
        |{"GAME MODE": ^{MENU_WIDTH}}|
        {"-" * SCREEN_WIDTH}
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * LEFT_PADDING}{'One Player': <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Two Players": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Go Back": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        {"-" * SCREEN_WIDTH}
        """)

        return mode_menu
