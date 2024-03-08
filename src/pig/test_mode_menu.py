"""Test for the ModeMenu class."""
import unittest
from mode_menu import ModeMenu


class TestModeMenu(unittest.TestCase):
    """Test for the ModeMenu class."""
    def setUp(self):
        self.menu = ModeMenu('main_menu', 'exit_menu')

    def test_is_instance(self):
        """Test if the menu is an instance of ModeMenu."""
        self.assertIsInstance(self.menu, ModeMenu)

    def test_is_subclass(self):
        """Test if the menu is a subclass of ModeMenu."""
        self.assertTrue(issubclass(ModeMenu, ModeMenu))


if __name__ == '__main__':
    unittest.main()
