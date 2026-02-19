
import unittest
from unittest.mock import patch
from src.finding_the_percentage.util import find_average


class TestFindPercentage(unittest.TestCase):

    @patch("builtins.input")
    def test_average_case(self, mock_input):
        mock_input.side_effect = [
            "1",
            "Akhil 80 90 100",
            "Akhil"
        ]

        result = find_average()
        self.assertEqual(result, 90.0)


if __name__ == "__main__":
    unittest.main()

