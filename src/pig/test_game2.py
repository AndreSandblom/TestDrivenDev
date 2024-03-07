"""Unit testing for game2 class."""

import unittest
import textwrap
from unittest.mock import patch
from game2 import Game
from player import Player
from intelligence import Intelligence


class TestGame(unittest.TestCase):
    """Test the Game Class."""

    def setUp(self):
        """Create two players for testing."""
        self.single_game = Game(Player("Jenny"), Intelligence("easy"))
        self.double_game = Game(Player("Anna"), Player("William"))
        self.Jenny = self.single_game.player1.get_name()
        self.Computer = self.single_game.player2
        # self.Anna = self.double_game.player1.get_name()
        # self.William = self.double_game.player2.get_name()

    def test__init__(self):
        """Test if the games are instances of Game class."""
        self.assertIsInstance(self.single_game, Game)
        self.assertIsInstance(self.double_game, Game)

    def test_do_roll_is_1(self):
        """Test when roll is 1 in single game."""
        with patch.object(self.single_game, "roll_dice", return_value=1):
            # Assuming player1 is the current player
            self.single_game.do_roll("roll")
            self.assertEqual(self.single_game.get_current_player().turn_total, 0)

    def test_do_roll_is_not_1(self):
        """Test when roll is not 1 in single game."""
        with patch.object(self.single_game, "roll_dice", return_value=4):
            # Assuming player1 is the current player
            init_turn_total = self.single_game.get_current_player().turn_total
            self.single_game.do_roll("roll")
            self.assertEqual(self.single_game.get_current_player().turn_total,
                             init_turn_total + 4)

    def test_do_roll_is_1_2(self):
        """Test when roll is 1 in double game."""
        with patch.object(self.double_game, "roll_dice", return_value=1):
            # Assuming player1 is the current player
            self.double_game.do_roll("roll")
            self.assertEqual(self.double_game.get_current_player().turn_total, 0)

    def test_do_roll_is_not_1_2(self):
        """Test when roll is not 1 in double game."""
        with patch.object(self.double_game, "roll_dice", return_value=4):
            # Assuming player1 is the current player
            init_turn_total = self.double_game.get_current_player().turn_total
            self.double_game.do_roll("roll")
            self.assertEqual(self.double_game.get_current_player().turn_total,
                             init_turn_total + 4)
    
    def test_do_hold(self):
        # Not sure how to implement
        pass

    def test_check_end_of_game(self):
        # Not sure how to implement
        pass
    
    def test_do_edit_name(self):
        pass

    def test_do_cheat(self):
        pass

    def test_do_restart(self):
        pass

    def do_quit(self):
        pass

    def test_has_won(self):
        """Test method returns True while score >= 100 else False."""
        self.assertTrue(self.single_game.has_won(101))
        self.assertTrue(self.double_game.has_won(100))
        self.assertFalse(self.single_game.has_won(99))
        self.assertFalse(self.double_game.has_won(99))

    def test_get_current_player(self):
        """Test that player1 is returned after a game is initiated."""
        self.assertEqual(
            self.single_game.get_current_player(), self.single_game.player1)

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
        if self.single_game.player1_turn:
            self.single_game.set_score(20)
            self.assertEqual(self.single_game.score1, 20)
        else:
            self.single_game.set_score(20)
            self.assertEqual(self.single_game.score2, 20)

    def test_change_turn(self):
        """Test the turn is changed to player2."""
        self.single_game.change_turn()
        self.assertFalse(self.single_game.player1_turn)

    def test_roll_dice(self):
        """Test if 1 <= returned dice num <= 6."""
        returned_num = self.single_game.roll_dice()
        expected = 1 <= returned_num <= 6
        self.assertTrue(expected)
        returned_num = self.double_game.roll_dice()
        expected = 1 <= returned_num <= 6
        self.assertTrue(expected)

    def test_cheat(self):
        """Test that players' score increments by 50."""
        if self.single_game.player1_turn:
            self.single_game.cheat()
            self.assertEqual(self.single_game.score1, 50)
        else:
            self.single_game.cheat()
            self.assertEqual(self.single_game.score2, 50)

    def test_get_winning_score(self):
        """Test that the initial winning score is 100."""
        self.assertEqual(self.single_game.get_winning_score(), 100)
        self.assertEqual(self.double_game.get_winning_score(), 100)

    def test_play_computer_turn(self):
        """"""
        pass

if __name__ == "__main__":
    unittest.main()








# def test_start(self):
    #     """Test the print is the same from the method."""
    #     self.single_game.set_score(10, 20)
    #     self.single_game.current_roll = 3

    #     expected = textwrap.dedent("""
    #     --------------------------------------------------
    #     |                  PIG                           |
    #     --------------------------------------------------
    #     |                                                |
    #     |    Player 1: Alice     Player 2: Bob           |
    #     |    Score: 10           Score: 20               |
    #     |                                                |
    #     |                   DIE ROLL                     |
    #     |        -------                                 |
    #     |    Alice's Turn                                |
    #     |    Turn Total: 0                               |
    #     |    roll or hold?                               |
    #     |                                                |
    #     --------------------------------------------------
    #     """)
    #     self.assertEqual(
    #         self.single_game.start(self.Jenny, self.Computer), expected)
