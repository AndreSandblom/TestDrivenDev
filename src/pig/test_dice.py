import unittest
from dice import Dice1,Dice2


class TestDice(unittest.TestCase):

    def test_dice_roll(self):
        dice = Dice1()
        roll = dice.roll()
        self.assertTrue(1 <= roll <= 6)
        dice2 = Dice2(12)
        roll2 = dice2.roll()
        self.assertTrue(1 <= roll2 <= 12)


if __name__ == '__main__':
    unittest.main()
