'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))
