class Solution:
    def numIdenticalPairs(self, nums):
        good_pairs = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs


sol = Solution()
print(sol.numIdenticalPairs([1, 1, 1, 1]))
