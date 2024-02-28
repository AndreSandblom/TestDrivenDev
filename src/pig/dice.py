import random

# Alternative 1 - Dice with 6 sides and a roll function
class Dice1:
    def __init__(self):
        self.dice_list = [1, 2, 3, 4, 5, 6]
    def roll(self):
        return random.choice(self.dice_list)

# Alternative 2 - Dice with any number of sides and a roll function
class Dice2:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        start = 1
        self.dice_num_list = [start + i for i in range(self.num_of_sides)]
    def roll(self):
        return random.choice(self.dice_num_list)


# dice = Dice(12)    
# print(dice.roll())