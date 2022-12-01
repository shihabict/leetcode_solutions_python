class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []

        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if j != i and nums[i] > nums[j]:
                    c += 1
            result.append(c)
        return result


sol = Solution()

print(sol.smallerNumbersThanCurrent([6, 5, 4, 8]))
