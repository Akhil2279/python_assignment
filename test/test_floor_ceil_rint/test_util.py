
import unittest
import numpy as np
from src.floor_ceil_rint.util import process_array


class TestProcessArray(unittest.TestCase):

    def test_single_value(self):
        values = [2.5]

        floor_values, ceil_values, rint_values = process_array(values)

        self.assertTrue((floor_values == np.array([2.])).all())
        self.assertTrue((ceil_values == np.array([3.])).all())
        self.assertTrue((rint_values == np.array([2.])).all())


if __name__ == "__main__":
    unittest.main()


