from typing import List


class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)+1


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 2))
