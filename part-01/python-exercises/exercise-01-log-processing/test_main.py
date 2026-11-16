
import unittest

from main import (
    get_unique_usernames,
    get_login_statistics,
)


class TestLogProcessing(unittest.TestCase):

    def test_unique_usernames(self):
        """Test that duplicate usernames are removed."""
        usernames = ["alice", "bob", "alice", "charlie", "bob"]

        result = get_unique_usernames(usernames)

        expected = {"alice", "bob", "charlie"}

        self.assertEqual(result, expected)

    def test_empty_usernames(self):
        """Test that an empty list returns an empty set."""
        usernames = []

        result = get_unique_usernames(usernames)

        expected = set()

        self.assertEqual(result, expected)

    def test_all_unique_usernames(self):
        """Test a list with no duplicates."""
        usernames = ["alice", "bob", "charlie", "dave"]

        result = get_unique_usernames(usernames)

        expected = {"alice", "bob", "charlie", "dave"}

        self.assertEqual(result, expected)

    def test_login_statistics(self):
        """Test that login statistics are calculated correctly."""

        # Arrange
        usernames = ["alice", "bob", "alice", "charlie", "bob"]

        expected = {
            "total_attempts": 5,
            "unique_users": 3
        }

        # Act
        result = get_login_statistics(usernames)

        # Assert
        self.assertEqual(result, expected)

    def test_login_statistics_empty(self):
        """Test statistics when there are no login attempts."""

        result = get_login_statistics([])

        expected = {
            "total_attempts": 0,
            "unique_users": 0
        }

        self.assertEqual(result, expected)

    def test_login_statistics_all_unique(self):
        """Test statistics when every username is unique."""

        usernames = ["alice", "bob", "charlie"]

        result = get_login_statistics(usernames)

        expected = {
            "total_attempts": 3,
            "unique_users": 3
        }

        self.assertEqual(result, expected)

    def test_whitespace_handling(self):
        """Test a list containing usernames with whitespace"""

        usernames = [" alice", "alice ", " bob ", "charlie"]

        result = get_unique_usernames(usernames)

        expected = {"alice", "bob", "charlie"}

        self.assertEqual(result, expected)

    def test_blank_usernames(self):
        """Test a list containing empty or whitespace-only usernames."""

        usernames = ["", "alice", "  "]

        result = get_unique_usernames(usernames)

        expected = {"alice"}

        self.assertEqual(result, expected)

    def test_single_username(self):
        """Test a list containing only one username."""

        usernames = ["alice"]

        result = get_unique_usernames(usernames)

        self.assertEqual(result, {"alice"})


if __name__ == "__main__":
    unittest.main()
