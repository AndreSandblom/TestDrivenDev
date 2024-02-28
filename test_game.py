"""Unit testing."""

import unittest
from game import Game
from player import Player

class TestGame(unittest.TestCase):
    """Test the Game class."""

    def setUp(self) -> None:
        """Create two players for testing."""
        self.player1 = Player("A")
        self.player2 = Player("B")
        self.single_game = Game(self.player1)
        self.double_game = Game(self.player1, self.player2)

    def test_init_(self):
        """Test if the games are instances of Game class"""
        self.assertIsInstance(self.single_game, Game)
        self.assertIsInstance(self.double_game, Game)

    def test_roll_dice(self):
        """Test if 1 <= returned dice num <= 6."""
        returned_num = self.single_game.roll_dice()
        expected = 1 <= returned_num <= 6
        self.assertTrue(expected)
        returned_num = self.double_game.roll_dice()
        expected = 1 <= returned_num <= 6
        self.assertTrue(expected)

    def test_intelligence_roll_dice(self):
        """Test """
        pass

    def test_get_score(self):
        """Test the initial scores of players are 0."""
        default_0 = self.single_game.get_score(self.player1)
        self.assertEqual(default_0, 0)
        default_0 = self.double_game.get_score(self.player1)
        self.assertEqual(default_0, 0)
        default_0 = self.double_game.get_score(self.player2)
        self.assertEqual(default_0, 0)

    def test_increment_score(self):
        """"""