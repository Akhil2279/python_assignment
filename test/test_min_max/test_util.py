
import unittest
from unittest.mock import patch
from src.min_max.util import array

class TestArrayFunction(unittest.TestCase):

    @patch("builtins.input")
    def test_array_result(self, mock_input):

        mock_input.side_effect = [
            "2 2",
            "1 2",
            "3 4"
        ]
        result = array()
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
