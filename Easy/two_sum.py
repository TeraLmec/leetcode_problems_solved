class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
    
# Test_cases    

import unittest

class TestTwoSum(unittest.TestCase):
    def test_empty_list(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([], 5), [])

    def test_single_element_list(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2], 4), [])

    def test_two_element_list(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7], 9), [0, 1])

    def test_no_solution(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 3, 4], 10), [])

    def test_multiple_solutions(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 2, 3, 3], 4), [0, 1])

    def test_large_list(self):
        solution = Solution()
        nums = [i for i in range(1000)]
        self.assertEqual(solution.twoSum(nums, 999), [0, 999])

    def test_negative_numbers(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([-2, -7], -9), [0, 1])

    def test_zero(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([0, 0], 0), [0, 1])

if __name__ == '__main__':
    unittest.main()