"""This module contains the Intelligence class."""
import time
from player import Player


class Intelligence(Player):
    """Class for the computer player. Inherits from Player class."""

    def __init__(self, difficulty, name="Computer"):
        super().__init__(name)
        self.difficulty = difficulty

    def play(self, game):
        """The computer player's turn."""
        self.turn_total = 0
        ongoing = True
        while ongoing:
            game.current_roll = game.roll_dice()
            if self.check_roll(game.current_roll) != 0:
                ongoing = self.check_difficulty_action(game)
            else:
                ongoing = False

            print(game.start(game.player1, self))
            time.sleep(1)

    def check_roll(self, roll_number):
        match(roll_number):
            case 1:
                self.turn_total = 0
            case _:
                self.turn_total += roll_number

        return self.turn_total

    def check_difficulty_action(self, game):
        match(self.difficulty):
            case "easy":
                if self.turn_total >= 20:
                    return False
            case "normal":
                if self.turn_total >= 25:
                    return False
            case "hard":
                if game.get_score_1() > 70 or game.get_score_2() > 70:
                    pass
                elif self.turn_total >= 21 + abs(game.get_score_1()
                                                 - game.get_score_2()) / 8:
                    return False

        return True
