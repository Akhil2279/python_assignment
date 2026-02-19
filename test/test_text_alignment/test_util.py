
import unittest
from unittest.mock import patch
from io import StringIO
from src.text_alignment.util import print_logo


class TestPrintLogo(unittest.TestCase):

    @patch("builtins.input", return_value="1")
    @patch("sys.stdout", new_callable=StringIO)
    def test_logo_small(self, mock_output, mock_input):

        print_logo()

        output = mock_output.getvalue()
        lines = output.strip().split("\n")

        self.assertEqual(len(lines), 7)
        self.assertIn("H", output)

if __name__ == "__main__":
    unittest.main()


