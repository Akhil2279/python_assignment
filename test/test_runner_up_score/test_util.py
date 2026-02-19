
import unittest
from unittest.mock import patch
from src.runner_up_score.util import find_runner_up


class TestFindRunnerUp(unittest.TestCase):

    @patch("builtins.input")
    def test_runner_score(self, mock_input):
        mock_input.side_effect = [
            "5",
            "2 3 6 6 5"
        ]

        result = find_runner_up()
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
