
class Player:

    def __init__(self, name: str):
        self.name = name
        self.played_game = 0
        self.won_games = 0

    def get__player_score(self):
        print('Player:', self.name)
        print('Amount of games:', self.played_game)
        print('Amount of won games:', self.won_games)

    def add_game(self):
        self.played_game += 1

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
