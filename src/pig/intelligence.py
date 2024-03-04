from player import Player
from dice import Dice


class Intelligence(Player):
    
    def __init__(self, difficulty, name="Computer"):
        super().__init__(name)
        self.difficulty = difficulty
        self.dice = Dice(6)

    def play(self, game):
        turn_total = 0

        while True:
            roll = self.dice.roll()
            print(f"Computer rolled a {roll}!")

            match(roll):
                case 1:
                    turn_total = 0
                    return turn_total
                case _:
                    turn_total += roll
           
            match(self.difficulty):
                case "easy":
                    if turn_total >= 20:
                        return turn_total
                case "normal":
                    if turn_total >= 25:
                        return turn_total
                case "hard":
                    if game.get_score_1() > 70 or game.get_score_2() > 70:
                        continue
                    elif turn_total >= 21 + abs(game.get_score_1() - game.get_score_2()) / 8:
                        return turn_total
       


        