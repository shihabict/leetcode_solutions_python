class Solution:
    def buildArray(self, nums):
        ans = []
        for i in range(0, len(nums)):
            index = nums[i]
            ans.append(nums[index])
        return ans


sol = Solution()
print(sol.buildArray([0, 2, 1, 5, 3, 4]))
