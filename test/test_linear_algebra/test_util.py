
import unittest
from unittest.mock import patch
from src.linear_algebra.util import calculate_determinant


class TestCalculateDeterminant(unittest.TestCase):

    @patch("builtins.input")
    def test_2x2_matrix(self, mock_input):

        mock_input.side_effect = [
            "2",
            "1 2",
            "3 4"
        ]

        result = calculate_determinant()
        self.assertEqual(result, -2.00)

if __name__ == "__main__":
    unittest.main()
