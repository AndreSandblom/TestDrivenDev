"""This module contains the Intelligence class."""

from player import Player
from dice import Dice


class Intelligence(Player):
    """Class for the computer player. Inherits from Player class."""

    def __init__(self, difficulty, name="Computer"):
        super().__init__(name)
        self.difficulty = difficulty

    def play(self, game):
        """The computer player's turn."""
        turn_total = 0

        while True:
            roll = Dice.roll()
            print(f"Computer rolled a {roll}!")

            match (roll):
                case 1:
                    turn_total = 0
                    return turn_total
                case _:
                    turn_total += roll

            match (self.difficulty):
                case "easy":
                    if turn_total >= 20:
                        return turn_total
                case "normal":
                    if turn_total >= 25:
                        return turn_total
                case "hard":
                    if game.score1 > 70 or game.score2 > 70:
                        continue
                    elif turn_total >= 21 + abs(game.score1 - game.score2) / 8:
                        return turn_total
