"""File to test methods"""

import unittest
import os
from highscore import Highscore
from player import Player


class TestHighscore(unittest.TestCase):
    """Test class for highscore module."""

    def setUp(self):
        """Create two players for testing."""
        self.player_list = [Player("Nisse"), Player("Stina")]
        self.path_name = "test.file"
        self.test_file = Highscore(self.path_name)
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")

    def tearDown(self):
        """Remove the test file."""
        try:
            os.remove(self.path_name)
        except FileNotFoundError:
            pass

    def test_load_empty_high_score(self):
        """Test load_high_score method"""
        self.assertEqual(self.test_file.load_highscore(), [])

    def test_save_highscore(self):
        """Test save_high_score method"""
        self.test_file.save_highscore(self.player_list)
        self.assertTrue(os.path.exists(self.test_file.filename))

    def test_load_highscore_nonexisting_fil(self):
        """Test load_high_score method"""
        try:
            os.remove(self.path_name)
        except FileNotFoundError:
            pass
        test = self.test_file.load_highscore()
        self.assertEqual(test, [])

    def test_sort_player_highscore(self):
        """Test sort_player_highscore method"""
        test_list1 = [self.player1, self.player2]
        self.player2.add_win()
        self.player2.add_win()
        self.player1.add_win()
        test_list2 = self.test_file.sort_player_highscore(test_list1)
        self.assertEqual(test_list2[0].name, "Player2")


if __name__ == "__main__":
    unittest.main()
