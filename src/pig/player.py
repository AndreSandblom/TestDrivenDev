"""Player Module for the Pig game."""


class Player:
    """Player class for the Pig game."""

    def __init__(self, name: str):
        """Initialize the player with a name."""
        self.name = name
        self.played_games = 0
        self.won_games = 0

    def __str__(self) -> str:
        return f'Player: {self.name}'

    def get_player_score(self):
        """Return the player's name, played and won games."""
        score_info = f'Player: {self.name}\n'
        score_info += f'Amount of games: {self.played_games}\n'
        score_info += f'Amount of won games: {self.won_games}\n'
        return score_info

    def add_game(self):
        """Add a played game to the player."""
        self.played_games += 1

    def add_win(self):
        """Add a won game to the player."""
        self.won_games += 1

    def reset_games(self):
        """Reset the player's played and won games."""
        self.played_games = 0
        self.won_games = 0

    def get_name(self):
        """Return the player's name."""
        return self.name

    def change_name(self, new_name):
        """Change the player's name."""
        self.name = new_name
        return self.name

    def print_player_highscore(self, list_of_players):
        """"Sort the players by wins & print the highscore list of players."""
        sorted_players = sorted(
            list_of_players, key=lambda player: player.won_games, reverse=True)
        print('Here are the Highscore list of players:')
        for player in sorted_players:
            score = player.get_player_score()
            print(score)
