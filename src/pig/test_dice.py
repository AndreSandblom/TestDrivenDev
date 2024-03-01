import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    """Test the Dice class."""

    def setUp(self) -> None:
        """Create a dice."""
        self.dice = Dice(6)

    def test__init__(self):
        self.assertIsInstance(self.dice, Dice)
    
    def test_roll(self):
        returned = self.dice.roll()
        expected = 1 <= returned <= 6
        self.assertTrue(expected)

    