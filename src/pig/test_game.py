"""Unit testing."""

import unittest
from game import Game
from player import Player
from intelligence import Intelligence


class TestGame(unittest.TestCase):
    """Test the Game class."""

    def setUp(self) -> None:
        """Create two players for testing."""
        self.single_game = Game(Player("Jenny"), Intelligence()) 
        self.double_game = Game(Player("Anna"), Player("William"))
        self.Jenny = self.single_game.player1.get_name()
        self.Computer = self.single_game.player2
        self.Anna = self.double_game.player1.get_name()
        self.William = self.double_game.player2.get_name()

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

    def test_get_score(self):
        """Test the initial scores of players are 0."""
        default_0 = self.single_game.get_score_1()
        self.assertEqual(default_0, 0)
        default_0 = self.double_game.get_score_1()
        self.assertEqual(default_0, 0)
        default_0 = self.double_game.get_score_2()
        self.assertEqual(default_0, 0)

    def test_set_score(self):
        """Test if score can be set manually."""
        self.single_game.set_score(98, 85)
        self.double_game.set_score(98, 85)
        self.assertEqual(self.single_game.get_score_1(), 98)
        self.assertEqual(self.single_game.get_score_2(), 85)
        self.assertEqual(self.double_game.get_score_1(), 98)
        self.assertEqual(self.double_game.get_score_2(), 85)

    def test_increment_and_determine(self):
        """Test if the score can be incremented and determined if has won."""
        self.single_game.set_score(98, 85)
        self.double_game.set_score(98, 85)
        single_dic = self.single_game.increment_and_determine_1(6)
        expected = {"Jenny": 104, "Computer": 85}
        self.assertEqual(single_dic, expected)
        double_dic = self.double_game.increment_and_determine_1(6)
        expected = {"Anna": 104, "William": 85}
        self.assertEqual(double_dic, expected)
        self.assertEqual(self.single_game.increment_and_determine_2(6), 0)
        self.assertEqual(self.double_game.increment_and_determine_2(6), 0)

    def test_has_won(self):
        """Test that when score >= 100, the method returns True."""
        self.assertFalse(self.single_game.has_won(99))
        self.assertTrue(self.single_game.has_won(100))
        self.assertTrue(self.single_game.has_won(105))

    def test_winner(self):
        """Test that a dictionary is returned when winning."""
        self.single_game.set_score(101, 99)
        winning_dict = {self.Jenny: self.single_game.get_score(self.Jenny),
                        self.Computer: self.single_game.get_score_2()}
        self.assertEqual(winning_dict, self.single_game.winner())
        self.double_game.set_score(99, 101)
        winning_dict = {self.William: self.double_game.get_score_2(),
                        self.Anna: self.double_game.get_score_1()}
        self.assertEqual(winning_dict, self.double_game.winner())

    def test_cheat(self):
        """Test that winnig score can be set to 50."""
        self.single_game.cheat()
        self.double_game.cheat()
        self.assertEqual(self.single_game.get_winning_score(), 50)
        self.assertEqual(self.double_game.get_winning_score(), 50)

    def test_get_winning_score(self):
        """Test correct winning score is returned."""
        self.assertEqual(self.single_game.get_winning_score(), 100)
        self.assertEqual(self.double_game.get_winning_score(), 100)
