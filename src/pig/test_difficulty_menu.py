"""Test for DifficultyMenu class."""
import unittest
from difficulty_menu import DifficultyMenu


class TestDifficultyMenu(unittest.TestCase):
    """Test for the DifficultyMenu class."""
    def setUp(self):
        self.menu = DifficultyMenu('mode_menu', 'exit_menu')
        self.difficulty = 'easy'

    def test_is_instance(self):
        """Test if the menu is an instance of DifficultyMenu."""
        self.assertIsInstance(self.menu, DifficultyMenu)

    def test_is_subclass(self):
        """Test if the menu is a subclass of DifficultyMenu."""
        self.assertTrue(issubclass(DifficultyMenu, DifficultyMenu))


if __name__ == '__main__':
    unittest.main()
