"""Module for handling highscore list of players."""

import pickle
from player import Player


class Highscore:
    """Class for handling highscore list of players."""

    def __init__(self, filename: str):
        self.filename = filename

    def load_highscore(self) -> list[Player]:
        """Load highscore list from file and return it. If file does not exist,
        return an empty list."""
        try:
            with open(self.filename, "rb") as history:
                temp_list = pickle.load(history)
            sorted_list = self.sort_player_highscore(temp_list)
            return sorted_list
        except FileNotFoundError:
            return []

    def save_highscore(self, list_of_player):
        """Save highscore list to file."""
        with open(self.filename, "wb") as high_score:
            pickle.dump(list_of_player, high_score)

    def sort_player_highscore(self, list_of_players):
        """ "Sort the players by wins & print the highscore list of players."""
        sorted_players = sorted(
            list_of_players, key=lambda player: player.won_games, reverse=True
        )
        return sorted_players
