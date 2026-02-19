

import unittest
from unittest.mock import patch
from src.no_idea.util import calculate_happiness


class TestCalculateHappiness(unittest.TestCase):

    @patch("builtins.input")
    def test_happiness(self, mock_input):

        mock_input.side_effect = [
            "3 2",
            "1 5 3",
            "3 1",
            "5 7"
        ]

        result = calculate_happiness()
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
