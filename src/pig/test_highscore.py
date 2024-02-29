"""File to test methods"""
import unittest
import os
from highscore import Highscore
from player import Player


class TestHighscore(unittest.TestCase):
    """Test class for highscore module."""

    def setUp(self):
        """Create two players for testing."""
        self.player_list = [Player('Nisse'), Player('Stina')]
        self.path_name = 'test.file'
        self.test_file = Highscore(self.path_name)

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


if __name__ == "__main__":
    unittest.main()
