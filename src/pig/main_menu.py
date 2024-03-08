"""Main module for the game PIG"""
import os
import sys
import cmd
import textwrap
from mode_menu import ModeMenu
from highscore import Highscore
SCREEN_WIDTH = 60
MENU_WIDTH = SCREEN_WIDTH - 2
LEFT_PADDING = 23


class MainMenu(cmd.Cmd):
    """The main menu for the game."""
    prompt = textwrap.dedent("""\
        Type a valid command or 'help' to see the existing commands.
        >>> """)
    file = "highscore.pkl2"

    def do_start(self, arg):
        """Start the game."""
        mode = ModeMenu(self.display_main_menu(), self.exit_game)
        mode.cmdloop(mode.display_mode_menu())

    def do_rules(self, arg):
        """Read the rules of the game."""
        self.display_rules()

    def do_highscores(self, arg):
        """Display the high scores."""
        self.display_highscores()

    def do_exit(self, arg):
        """Exit the game."""
        self.exit_game()

    def do_menu(self, arg):
        """Return to the main menu."""
        self.clear_terminal()
        self.cmdloop()

    def clear_terminal(self):
        """Clear the terminal."""

        if os.name == 'nt':
            # For Windows
            _ = os.system('cls')
        else:
            # For Unix-like systems (macOS, Linux)
            _ = os.system('clear')

    def display_main_menu(self):
        """Display the main menu of the game."""

        self.clear_terminal()

        main_menu = textwrap.dedent(f"""
        {"-" * SCREEN_WIDTH}
        |{"PIG": ^{MENU_WIDTH}}|
        {"-" * SCREEN_WIDTH}
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * LEFT_PADDING}{'Start Game': <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Read Rules": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"High Scores": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * LEFT_PADDING}{"Exit Game": <{MENU_WIDTH-LEFT_PADDING}}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        |{" " * MENU_WIDTH}|
        {"-" * SCREEN_WIDTH}
        """)

        return main_menu

    def display_rules(self):
        """Display the rules of the game."""
        self.clear_terminal()
        print()
        print("-" * SCREEN_WIDTH)
        print(f"|{'RULES': ^{MENU_WIDTH}}|")
        print("-" * SCREEN_WIDTH)
        print("|                                                          |")
        print("|  Each turn, a player repeatedly rolls a die until either |")
        print("|  a 1 is rolled or the player decides to HOLD.            |")
        print("|                                                          |")
        print("|  ¤ If the player rolls a 1, they score nothing and it    |")
        print("|    becomes the next player's turn.                       |")
        print("|  ¤ If the player rolls any other number, it is added to  |")
        print("|    their turn total and the player's turn continues.     |")
        print("|  ¤ If a player chooses to HOLD, their turn total is added|")
        print("|    to their score, and it becomes the next player's turn.|")
        print("|                                                          |")
        print("|  The first player to score 100 or more points wins.      |")
        print("|                                                          |")
        print("|                   Enter \"menu\" to go back                |")
        print("-" * SCREEN_WIDTH)
        print()

    def display_highscores(self):
        """Display the high scores."""
        hs = Highscore(self.file)
        highscores = hs.load_highscore()

        self.clear_terminal()
        print()
        print("-" * SCREEN_WIDTH)
        print(f"|{'HIGH SCORES': ^{MENU_WIDTH}}|")
        print("-" * SCREEN_WIDTH)
        print(f"|{' ' * MENU_WIDTH}|")
        print(f"|{' ' * 10}{'PLAYER':15}{'PLAYED GAMES':15}"
              + f"{'WON GAMES':{MENU_WIDTH-40}}|")
        print(f"|{' ' * MENU_WIDTH}|")

        if len(highscores) >= 10:
            for h in range(10):
                print("|" + " " * 10 + f"{highscores[h].name:15}"
                      + f"{highscores[h].played_games:15}"
                      + f"{highscores[h].won_games: <{MENU_WIDTH-40}}" + "|")
        else:
            for h in highscores:
                print("|" + " " * 10 + f"{h.name:15}"
                      + f"{h.played_games:<15}"
                      + f"{h.won_games: <{MENU_WIDTH-40}}" + "|")
            for slot in range(10 - len(highscores)):
                print("|" + " " * 10 + f"{'-----':15}"
                      + f"{'0':15}"
                      + f"{'0': <{MENU_WIDTH-40}}" + "|")

        print(f"|{' ' * MENU_WIDTH}|")
        print(f"|{'Enter menu to go back':^{MENU_WIDTH}}|")
        print(f"|{' ' * MENU_WIDTH}|")
        print("-" * SCREEN_WIDTH)

    def exit_game(self):
        """Exit the game."""
        self.clear_terminal()
        empty_line = f"|{' ' * MENU_WIDTH}|\n"
        print()
        print("-" * SCREEN_WIDTH)
        print(f"|{'GOODBYE!': ^{MENU_WIDTH}}|")
        print("-" * SCREEN_WIDTH)
        print(empty_line * 6, end='')
        print(f"|{'Thank you for playing PIG!': ^{MENU_WIDTH}}|")
        print(f"|{'See you soon!': ^{MENU_WIDTH}}|")
        print(empty_line * 6, end='')
        print("-" * SCREEN_WIDTH)
        sys.exit()


if __name__ == "__main__":
    menu = MainMenu()
    MainMenu().cmdloop(menu.display_main_menu())
