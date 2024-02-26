
class Player:

    def __init__(self, name: str):
        self.name = name
        self.played_games = 0
        self.won_games = 0

    def get_player_score(self):
        score_info = f'Player: {self.name}\n'
        score_info += f'Amount of games: {self.played_games}\n'
        score_info += f'Amount of won games: {self.won_games}\n'
        return score_info

    def add_game(self):
        self.played_games += 1

    def add_win(self):
        self.won_games += 1

    def reset_games(self):
        self.played_games = 0
        self.won_games = 0

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name
        return self.name
