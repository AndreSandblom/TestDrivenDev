"""Unit tests for the intelligence module."""
import unittest
from intelligence import Intelligence
from game2 import Game
from dice import Dice
from player import Player


class TestIntelligence(unittest.TestCase):
    """Test the Intelligence class."""
    def setUp(self):
        """Create an instance of the Intelligence class for testing."""
        self.intelligence = Intelligence("easy", "ComputerEasy")
        self.intelligence2 = Intelligence("normal", "ComputerNormal")
        self.intelligence3 = Intelligence("hard", "ComputerHard")
        self.player = Player("Player2")
        self.game = Game(self.intelligence3, "Player2", exit_menu=False)
        self.dice = Dice(6)

    def test_intelligence_instance(self):
        """Test if the intelligence is an instance of Intelligence class."""
        self.assertIsInstance(self.intelligence, Intelligence)

    def test_intelligence_difficulty(self):
        """Test if the intelligence has the correct difficulty."""
        self.assertEqual(self.intelligence.difficulty, "easy")
        self.assertEqual(self.intelligence2.difficulty, "normal")
        self.assertEqual(self.intelligence3.difficulty, "hard")

    def test_check_roll(self):
        """Test if the turn total is updated correctly."""
        self.intelligence.check_roll(1)
        self.assertEqual(self.intelligence.turn_total, 0)
        self.intelligence.check_roll(3)
        self.assertEqual(self.intelligence.turn_total, 3)
        self.intelligence.check_roll(5)
        self.assertEqual(self.intelligence.turn_total, 8)

    def test_check_difficulty_action(self):
        """Test if the correct action is taken based on the difficulty."""
        self.assertTrue(self.intelligence.check_difficulty_action(None))
        self.assertTrue(self.intelligence2.check_difficulty_action(None))
        self.assertTrue(self.intelligence3.check_difficulty_action(self.game))

        self.intelligence.turn_total = 20
        self.assertFalse(self.intelligence.check_difficulty_action(None))

        self.intelligence2.turn_total = 25
        self.assertFalse(self.intelligence2.check_difficulty_action(None))

        self.intelligence3.turn_total = 20
        self.assertTrue(self.intelligence3.check_difficulty_action(self.game))

        self.intelligence3.turn_total = 21
        self.assertFalse(self.intelligence3.check_difficulty_action(self.game))

        self.intelligence3.turn_total = 21 + 3
        self.assertFalse(self.intelligence3.check_difficulty_action(self.game))

        self.intelligence3.turn_total = 70
        self.assertFalse(self.intelligence3.check_difficulty_action(self.game))


if __name__ == '__main__':
    unittest.main()
