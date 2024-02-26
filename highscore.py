import pickle
from player import Player
# Will contain the highscore, 2 functions- Show and set higscore


def load_high_score(filename) -> list[Player]:
    try:
        with open(filename, 'rb') as history:
            temp_list = pickle.load(history)
        return temp_list
    except FileNotFoundError:
        return []


def save_high_score(list_of_player, filename):
    with open(filename, 'wb') as high_score:
        pickle.dump(list_of_player, high_score)


def print_high_score(list_of_players):
    sorted_players = sorted(list_of_players, key=lambda player: player.won_games, reverse=True)
    print('Here are the Highscore list of players:')
    for player in sorted_players:
        score = player.get_player_score()
        print(score)


player1 = Player('Nisse')
player2 = Player('Stina')
player2.add_game()
player2.add_win()
player_list = []
player_list.append(player1)
player_list.append(player2)
print_high_score(player_list)
player1.add_game()
player1.add_win()
player1.add_game()
player1.add_win()
# save_high_score(player_list, "highscore.pkl2")
test_list = load_high_score("highscore.pkl2")
print_high_score(test_list)
player3 = Player('Marcus')
player3.add_game()
player3.add_game()
player3.add_game()
player3.add_win()
player3.add_win()
test_list.append(player3)
save_high_score(test_list, "highscore.pkl2")
test_list2 = load_high_score('highscore.pkl2')
print_high_score(test_list2)