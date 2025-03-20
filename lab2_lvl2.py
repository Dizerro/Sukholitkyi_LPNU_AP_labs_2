import unittest

def has_three_sum(arr, P):
    N = len(arr)

    for i in range(N - 1):
        seen = set()
        target = P - arr[i]
        
        for j in range(i + 1, N):
            if target - arr[j] in seen:
                return True
            seen.add(arr[j])        
    return False

class TestThreeSum(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(has_three_sum([1, 2, 3], 6))
        self.assertTrue(has_three_sum([5, 1, 4, 2, 3], 9))
        self.assertFalse(has_three_sum([1, 2, 4], 10))
        self.assertTrue(has_three_sum([10, 20, 30, 40, 50], 100))
        self.assertFalse(has_three_sum([1, 1, 1], 5))

unittest.main()