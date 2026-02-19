

import unittest
from unittest.mock import patch
import numpy as np
from src.mean_var_std.util import calculate_statistics


class TestCalculateStatistics(unittest.TestCase):

    @patch("builtins.input")
    def test_statistics(self, mock_input):

        mock_input.side_effect = [
            "2 2",
            "1 2",
            "3 4"
        ]

        mean_value, var_value, std_value = calculate_statistics()

        expected_mean = np.array([1.5, 3.5])
        expected_var = np.array([1., 1.])
        expected_std = np.std(np.array([[1, 2], [3, 4]]))

        self.assertTrue((mean_value == expected_mean).all())
        self.assertTrue((var_value == expected_var).all())
        self.assertAlmostEqual(std_value, expected_std)


if __name__ == "__main__":
    unittest.main()
