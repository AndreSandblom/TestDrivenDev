"""Main module for the Pig game."""
from main_menu import MainMenu

if __name__ == "__main__":
    menu = MainMenu()
    menu.cmdloop(menu.display_main_menu())
