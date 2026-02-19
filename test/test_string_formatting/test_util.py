
import unittest
from unittest.mock import patch
from io import StringIO
from src.string_formatting.util import print_formatted

class TestPrintFormatted(unittest.TestCase):

    @patch("builtins.input", return_value="2")
    @patch("sys.stdout", new_callable=StringIO)
    def test_print_format(self, mock_output, mock_input):

        print_formatted()

        expected_output = (
            " 1  1  1  1\n"
            " 2  2  2 10\n"
        )

        self.assertEqual(mock_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
