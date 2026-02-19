
import unittest
from unittest.mock import patch
from src.piling_up.util import piling_up


class TestPilingUp(unittest.TestCase):

    @patch("builtins.input")
    def test_piling_up_cases(self, mock_input):

        mock_input.side_effect = [
            "2",          # number of test cases

            "6",
            "4 3 2 1 3 4",  # Yes case

            "3",
            "1 3 2"         # No case
        ]

        result = piling_up()

        self.assertEqual(result, ["Yes", "No"])


if __name__ == "__main__":
    unittest.main()


