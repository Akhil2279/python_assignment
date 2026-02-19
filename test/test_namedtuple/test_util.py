
import unittest
from unittest.mock import patch
from io import StringIO
from src.collections_namedtuple.util import calculate_average

class TestCalculateAverage(unittest.TestCase):

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_average_marks(self, mock_output, mock_input):

        mock_input.side_effect = [
            "2",
            "ID MARKS NAME CLASS",
            "1 80 Akhil 10",
            "2 90 Rahul 10"
        ]

        calculate_average()
        self.assertEqual(mock_output.getvalue().strip(), "85.00")

if __name__ == "__main__":
    unittest.main()


