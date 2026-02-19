
import unittest
from unittest.mock import patch
from src.mutations.util import mutate_string


class TestMutateString(unittest.TestCase):

    @patch("builtins.input")
    def test_mutation(self, mock_input):
        mock_input.side_effect = [
            "abracadabra",
            "5 k"
        ]

        result = mutate_string()
        self.assertEqual(result, "abrackdabra")

if __name__ == "__main__":
    unittest.main()
