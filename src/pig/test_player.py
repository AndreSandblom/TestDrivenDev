"""This module contains unit tests for the Player class."""
import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def setUp(self) -> None:
        """Create two players for testing."""
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")

    def test_player_instance(self):
        """Test if the players are instances of the Player class."""
        self.assertIsInstance(self.player1, Player)
        self.assertIsInstance(self.player2, Player)

    def test_player_str(self):
        """Test if the players have the correct string representation."""
        self.assertEqual(str(self.player1), "Player: Player1")
        self.assertEqual(str(self.player2), "Player: Player2")

    def test_player_name(self):
        """Test if the players have the correct names."""
        self.assertEqual(self.player1.name, "Player1")
        self.assertEqual(self.player2.name, "Player2")

    def test_player_played_game(self):
        """Test if the players have played any games."""
        self.assertEqual(self.player1.played_games, 0)
        self.assertEqual(self.player2.played_games, 0)

    def test_player_won_game(self):
        """Test if the players have won any games."""
        self.assertEqual(self.player1.won_games, 0)
        self.assertEqual(self.player2.won_games, 0)

    def test_player_add_win(self):
        """Test if the players can add won games."""
        self.player1.add_win()
        self.assertEqual(self.player1.won_games, 1)
        self.player2.add_win()
        self.player2.add_win()
        self.assertEqual(self.player2.won_games, 2)

    def test_player_add_game(self):
        """Test if the players can add played games."""
        self.player1.add_game()
        self.assertEqual(self.player1.played_games, 1)
        self.player2.add_game()
        self.player2.add_game()
        self.assertEqual(self.player2.played_games, 2)

    def test_player_reset_score(self):
        """Test if the players can reset their scores."""
        self.player1.add_win()
        self.player1.add_game()
        self.player1.reset_games()
        self.assertEqual(self.player1.played_games, 0)
        self.assertEqual(self.player1.won_games, 0)
        self.player2.add_win()
        self.player2.add_win()
        self.player2.add_game()
        self.player2.add_game()
        self.player2.reset_games()
        self.assertEqual(self.player2.played_games, 0)
        self.assertEqual(self.player2.won_games, 0)

    def test_player_change_name(self):
        """Test if the players can change their names."""
        self.player1.change_name("PlayerOne")
        self.assertEqual(self.player1.name, "PlayerOne")
        self.player2.change_name("PlayerTwo")
        self.assertEqual(self.player2.name, "PlayerTwo")

    def test_player_get_name(self):
        """Test if the players can get their names."""
        self.assertEqual(self.player1.get_name(), "Player1")
        self.assertEqual(self.player2.get_name(), "Player2")

    def test_player_get_score(self):
        """Test if the players can get their scores."""
        self.assertEqual(
            self.player1.get_player_score(),
            "Player: Player1\nAmount of games: 0\nAmount of won games: 0\n"
        )
        self.assertEqual(
            self.player2.get_player_score(),
            "Player: Player2\nAmount of games: 0\nAmount of won games: 0\n"
        )


if __name__ == "__main__":
    unittest.main()
