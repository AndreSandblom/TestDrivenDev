import cmd, sys
from menu import Menu
from multipl import MultiGame
from singlepl import SingleGame
from player import Player
from intelligence import Intelligence

class MainShell(cmd.Cmd):
    prompt = "piggy >> "

    def __init__(self):
        self.menu = Menu()
        

    def do_main_menu(self):
        self.menu.display_main_menu()       # Choosing single/double game here

    def do_1(self):
        difficulty = input("Enter Easy/Normal/Hard for game mode: ")
        SingleGame(difficulty).cmdloop()

    def do_2(self):
        MultiGame().cmdloop()

    def do_rules(self):
        pass

    def do_mode_menu(self):
    
    def do_difficulty_menu(self):

    def


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))