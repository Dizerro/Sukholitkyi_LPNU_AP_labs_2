import unittest
from lab2_lvl2 import has_three_sum

class TestThreeSum(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(has_three_sum([1, 2, 3], 6))
        self.assertTrue(has_three_sum([5, 1, 4, 2, 3], 9))
        self.assertFalse(has_three_sum([1, 2, 4], 10))
        self.assertTrue(has_three_sum([10, 20, 30, 40, 50], 100))
        self.assertFalse(has_three_sum([1, 1, 1], 5))

unittest.main()