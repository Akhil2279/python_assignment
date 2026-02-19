
import unittest
from unittest.mock import patch
from io import StringIO
from src.merge_the_tools.util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_merge_tools(self, mock_output):

        merge_the_tools("AABCAAADA", 3)

        expected_output = "AB\nCA\nAD\n"
        self.assertEqual(mock_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()


