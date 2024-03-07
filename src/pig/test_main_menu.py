"""Test the main menu class."""
import unittest
from main_menu import MainMenu


class TestMainMenu(unittest.TestCase):
    """Test the main menu class."""
    def setUp(self):
        self.menu = MainMenu()

    def test_is_instance(self):
        """Test if the menu is an instance of MainMenu."""
        self.assertIsInstance(self.menu, MainMenu)


if __name__ == '__main__':
    unittest.main()
