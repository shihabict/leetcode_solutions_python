class Solution:
    def removeElement(self, nums, val):
        new_list = []
        while val in nums:
            nums.remove(val)
        return nums

sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2],2))
