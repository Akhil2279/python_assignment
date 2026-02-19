
import unittest
from src.calendar_module.util import find_day

class TestFindDay(unittest.TestCase):

    def test_known_date(self):
        result = find_day(8, 5, 2015)
        self.assertEqual(result, "WEDNESDAY")

    def test_leap_year(self):
        result = find_day(2, 29, 2020)
        self.assertEqual(result, "SATURDAY")

if __name__ == "__main__":
    unittest.main()
