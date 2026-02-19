
import unittest
from unittest.mock import patch
from src.iterables_iterators.util import probability_of_a


class TestProbabilityOfA(unittest.TestCase):

    @patch("builtins.input")
    def test_probability(self, mock_input):

        mock_input.side_effect = [
            "4",
            "a a c d",
            "2"
        ]

        result = probability_of_a()
        self.assertEqual(result, 0.8333)

if __name__ == "__main__":
    unittest.main()
