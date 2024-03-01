import random

class Dice:
    def __init__(self, num_of_sides):
        """Dice with any number of sides, 
        set 6 for this game,
        and a roll function."""
        num_of_sides = 6
        self.num_of_sides = num_of_sides
        start = 1
        self.dice_num_list = [start + i for i in range(self.num_of_sides)]

    def roll(self):
        """Return a random number."""
        return random.choice(self.dice_num_list)