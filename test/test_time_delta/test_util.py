
import unittest
from src.time_delta.util import time_delta


class TestTimeDelta(unittest.TestCase):

    def test_example_case(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        
        result = time_delta(t1, t2)
        self.assertEqual(result, 25200)

    def test_same_time(self):
        t1 = "Fri 01 Jan 2021 00:00:00 +0000"
        t2 = "Fri 01 Jan 2021 00:00:00 +0000"
        
        result = time_delta(t1, t2)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
