"""This module contains the Intelligence class."""
from player import Player
import time


class Intelligence(Player):
    """Class for the computer player. Inherits from Player class."""

    def __init__(self, difficulty, name="Computer"):
        super().__init__(name)
        self.difficulty = difficulty

    def play(self, game):
        """The computer player's turn."""

        while True:
            roll = game.roll_dice()
            game.current_roll = roll

            match(game.current_roll):
                case 1:
                    self.turn_total = 0
                    return self.turn_total
                case _:
                    self.turn_total += game.current_roll
            match(self.difficulty):
                case "easy":
                    if self.turn_total >= 20:
                        return self.turn_total
                case "normal":
                    if self.turn_total >= 25:
                        return self.turn_total
                case "hard":
                    if game.get_score_1() > 70 or game.get_score_2() > 70:
                        continue
                    elif self.turn_total >= 21 + abs(game.get_score_1()
                                                     - game.get_score_2()) / 8:
                        return self.turn_total
