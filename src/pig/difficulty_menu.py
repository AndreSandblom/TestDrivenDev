"""The difficulty menu module for the single player mode."""
import os
import cmd
import textwrap
from player import Player
from intelligence import Intelligence
from game2 import Game
SCREEN_WIDTH = 60
MENU_WIDTH = SCREEN_WIDTH - 2
LEFT_PADDING = 25


class DifficultyMenu(cmd.Cmd):
    """The difficulty menu for the single player mode."""""
    def __init__(self, mode_menu, exit_menu):
        super().__init__()
        self.mode_menu = mode_menu
        self.exit_menu = exit_menu
        self.difficulty = ''

    prompt = textwrap.dedent("""\
        Type a valid command or 'help' to see the existing commands.
        >>> """)

    def do_easy(self, arg):
        """Start a single player game with easy difficulty."""
        self.difficulty = "easy"
        game = self.create_game(self.difficulty)
        game.cmdloop(game.start(game.player1, game.player2))

    def do_normal(self, arg):
        """Start a single player game with normal difficulty."""
        self.difficulty = "normal"
        game = self.create_game(self.difficulty)
        game.cmdloop(game.start(game.player1, game.player2))

    def do_hard(self, arg):
        """Start a single player game with hard difficulty."""
        self.difficulty = "hard"
        game = self.create_game(self.difficulty)
        game.cmdloop(game.start(game.player1, game.player2))

    def do_back(self, arg):
        """Go back to the main menu."""
        self.clear_terminal()
        print(self.mode_menu)
        return True, arg

    def clear_terminal(self):
        """Clear the terminal."""

        if os.name == 'nt':
            # For Windows
            _ = os.system('cls')
        else:
            # For Unix-like systems (macOS, Linux)
            _ = os.system('clear')

    def display_difficulty_menu(self):
        """Display the single player difficulty menu."""
        self.clear_terminal()

        difficulty_menu = textwrap.dedent(f"""
        {"-" * SCREEN_WIDTH}
        |{"SINGLE PLAYER DIFFICULTY": ^{MENU_WIDTH}}|
        {"-" * SCREEN_WIDTH}
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * LEFT_PADDING}{'Easy': <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Normal": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Hard": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Go Back": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        {"-" * SCREEN_WIDTH}
        """)

        return difficulty_menu

    def create_game(self, difficulty):
        """Create a new game instance."""
        player1 = Player(input("Enter the player's name >>> ").capitalize())
        bot = Intelligence(difficulty)

        game = Game(player1, bot, self.exit_menu)

        return game
