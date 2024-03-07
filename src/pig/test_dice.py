"""Test the Dice class."""

import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    """Test the Dice class."""

    def setUp(self) -> None:
        """Create a dice."""
        self.dice = Dice(6)

    def test__init__(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.dice, Dice)

    def test_roll(self):
        """Test the roll method."""
        returned = self.dice.roll()
        expected = 1 <= returned <= 6
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
