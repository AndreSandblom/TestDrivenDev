import os
import sys
#import Game

def main():
    match(choose_main()):
        case "1":
            #Choose game mode: Single Player or Multiplayer
            match(choose_mode()):
                case "1":
                    #Single Player mode
                    name = input("Enter your name >>> ")
                    # player = Player(name)
                    # game = Game(player)
                    pass
                case "2":
                    #Multiplayer mode
                    # player1 = Player()
                    # player2 = Player()
                    # game = Game(player1, player2)
                    pass
                case "3":
                    main()
        case "2":
            #Display Rules
            display_rules()
            back = input()
            if back == "" or back != "":
                main()
        case "3":
            #Show High Scores
            pass
        case "4":
            #Exit Game
            exit_game()
                

def display_main_menu():
    clear_terminal()
    print("-------------------------------")
    print("|             PIG             |")
    print("-------------------------------")
    print("|                             |")
    print("|        1. Start Game        |")
    print("|        2. Read Rules        |")
    print("|        3. High Scores       |")
    print("|        4. Exit Game         |")
    print("|                             |")
    print("-------------------------------")
    print()

def choose_main():
    display_main_menu()
    menu_choice = input("Choose an option >>> ")
    valid_inputs = ["1", "2", "3", "4"]
    while menu_choice not in valid_inputs:
        validate_input(menu_choice, valid_inputs)
        menu_choice = input("Choose an option >>> ")

    return menu_choice

def display_mode_menu():
    clear_terminal()
    print("-------------------------------")
    print("|          GAME MODE          |")
    print("-------------------------------")
    print("|                             |")
    print("|        1. Single Player     |")
    print("|        2. Multiplayer       |")
    print("|        3. Go Back           |")
    print("|                             |")
    print("-------------------------------")
    print()

def choose_mode():
    display_mode_menu()
    mode_choice = input("Choose a game mode option >>> ")
    valid_inputs = ["1", "2", "3"]
    while mode_choice not in valid_inputs:
        validate_input(mode_choice, valid_inputs)
        mode_choice = input("Choose a game mode option >>> ")

    return mode_choice

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (macOS, Linux)
    else:
        _ = os.system('clear')

def exit_game():
        clear_terminal()
        print("-------------------------------")
        print("|  Thank you for playing PIG! |")
        print("|             Bye!            |")
        print("-------------------------------")
        sys.exit()

def validate_input(unchecked_input, valid_inputs):
    try:
        input = unchecked_input
        if input not in valid_inputs:
            raise ValueError
    except ValueError:
        print(f"Invalid option. Choose a number from {valid_inputs[0]} to {valid_inputs[-1]}.")
    
    return input

def display_rules():
    clear_terminal()
    print("-------------------------------------------------------------")
    print("|                           RULES                           |")
    print("-------------------------------------------------------------")
    print("|                                                           |")
    print("|  Each turn, a player repeatedly rolls a die until either  |")
    print("|  a 1 is rolled or the player decides to HOLD.             |")
    print("|                                                           |")
    print("|  ¤ If the player rolls a 1, they score nothing and it     |")
    print("|    becomes the next player's turn.                        |")
    print("|  ¤ If the player rolls any other number, it is added to   |")
    print("|    their turn total and the player's turn continues.      |")
    print("|  ¤ If a player chooses to HOLD, their turn total is added |")
    print("|    to their score, and it becomes the next player's turn. |")
    print("|                                                           |")
    print("|  The first player to score 100 or more points wins.       |")
    print("|                                                           |")
    print("|                   Press Enter to go back                  |")
    print("-------------------------------------------------------------")
    print()


if __name__ == "__main__":
    main()