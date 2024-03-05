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

    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu

    prompt = "Select an option >>> "

    def do_one(self, arg):
        difficulty = DifficultyMenu(self.display_mode_menu())
        DifficultyMenu(self.display_mode_menu()).cmdloop(difficulty.display_difficulty_menu())

    def do_two(self, arg):
        player1 = Player(input("Enter the name for Player 1 >>> "))
        player2 = Player(input("Enter the name for Player 2 >>> "))

        game = Game(player1, player2)
        Game(player1, player2).cmdloop(game.start(player1, player2))

    def do_back(self, arg):
        self.clear_terminal()
        print(self.main_menu)
        return True

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
