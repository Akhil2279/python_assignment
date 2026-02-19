
import unittest
from unittest.mock import patch
from src.word_orderd.util import count_words

class TestCountWords(unittest.TestCase):

    @patch("builtins.input")
    def test_word_count(self, mock_input):

        mock_input.side_effect = [
            "4",
            "apple",
            "banana",
            "apple",
            "orange"
        ]

        distinct_count, occurrences = count_words()

        self.assertEqual(distinct_count, 3)
        self.assertEqual(occurrences, [2, 1, 1])

if __name__ == "__main__":
    unittest.main()
